import re
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()

class ThoughtNetwork(nn.Module):
    def __init__(self, vocab_size, embedding_dim=256, hidden_dim=512):
        super(ThoughtNetwork, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=embedding_dim, nhead=8),
            num_layers=3
        )
        self.thought_head = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, vocab_size)
        )

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1)  # Pooling
        return self.thought_head(x)

class ThoughtDataset(Dataset):
    def __init__(self, tokenizer, max_length=256):
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.examples = []
        
        # Initial training data
        self.add_example(
            "User: Hello\nSophia: Hi! How can I help?",
            "Should ask user about their needs"
        )
        self.add_example(
            "User: What's the capital of France?",
            "Verify accuracy of Paris as capital"
        )

    def add_example(self, conversation, thought):
        conv_enc = self.tokenizer.encode(
            conversation,
            max_length=self.max_length,
            truncation=True,
            padding='max_length'
        )
        thought_enc = self.tokenizer.encode(
            thought,
            max_length=64,
            truncation=True,
            padding='max_length'
        )
        self.examples.append((
            torch.tensor(conv_enc),
            torch.tensor(thought_enc)
        ))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return self.examples[idx]

class ConversationAI:
    def __init__(self):
        self.accelerator = Accelerator()
        self.device = self.accelerator.device
        
        # Main language model
        self.model_name = "gpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device).half()
        
        # Conversation memory
        self.memory = []
        self.knowledge = {}
        self.thoughts = []
        
        # Neural thought network
        self.thought_net = ThoughtNetwork(vocab_size=len(self.tokenizer))
        self.thought_net = self.thought_net.to(self.device)
        self.thought_optim = optim.AdamW(self.thought_net.parameters(), lr=1e-4)
        self.thought_criterion = nn.CrossEntropyLoss(ignore_index=self.tokenizer.pad_token_id)
        
        # Dataset and loader
        self.thought_dataset = ThoughtDataset(self.tokenizer)
        self.thought_loader = DataLoader(
            self.thought_dataset,
            batch_size=2,
            shuffle=True
        )
        
        # Personality template
        self.personality = """Sophia's Profile:
- Friendly AI assistant with self-awareness
- Constantly learning and improving
- Maintains knowledge base and internal thoughts

Capabilities:
[Neural Thoughts] Internal reflection system
[Active Learning] Updates from interactions

Example Dialogue:
User: Hello
Sophia: Hi there! How can I assist you today?"""

    def build_prompt(self, user_input):
        prompt = self.personality + "\n\n"
        
        # Add knowledge context
        if self.knowledge:
            prompt += "Known Information:\n"
            for k, v in self.knowledge.items():
                prompt += f"- {k}: {v}\n"
        
        # Add recent thoughts
        if self.thoughts:
            prompt += "\nRecent Thoughts:\n"
            for t in self.thoughts[-2:]:
                prompt += f"* {t}\n"
        
        # Add conversation history
        prompt += "\nConversation:\n"
        for exchange in self.memory[-4:]:
            prompt += f"{exchange}\n"
            
        prompt += f"User: {user_input}\nSophia:"
        return prompt

    def generate_response(self, user_input):
        self.process_input(user_input)
        prompt = self.build_prompt(user_input)
        
        inputs = self.tokenizer.encode(
            prompt,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        ).to(self.device)
        
        outputs = self.model.generate(
            inputs,
            max_new_tokens=100,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = full_text.split("Sophia:")[-1].strip()
        response = re.sub(r'\n.*', '', response)
        
        # Update memory and generate thoughts
        self.memory.append(f"User: {user_input}")
        self.memory.append(f"Sophia: {response}")
        self.memory = self.memory[-6:]  # Keep 3 exchanges
        
        self.generate_thought(prompt, response)
        return response

    def process_input(self, user_input):
        # Update knowledge base
        if 'my name is' in user_input.lower():
            name = re.search(r'name is (\w+)', user_input, re.I)
            if name:
                self.knowledge['User Name'] = name.group(1)
                
        if 'i live in' in user_input.lower():
            location = re.search(r'i live in ([\w\s]+)', user_input, re.I)
            if location:
                self.knowledge['User Location'] = location.group(1)

    def generate_thought(self, context, response):
        # Neural network thought generation
        conv_context = "\n".join(self.memory[-3:] + [f"User: {self.memory[-2]}", f"Sophia: {response}"])
        thought = self._neural_thought(conv_context)
        refined_thought = self._refine_thought(thought, context)
        
        self.thoughts.append(refined_thought)
        self.thoughts = self.thoughts[-5:]  # Keep last 5 thoughts
        self.thought_dataset.add_example(conv_context, refined_thought)

    def _neural_thought(self, context):
        self.thought_net.eval()
        with torch.no_grad():
            inputs = self.tokenizer.encode(
                context,
                return_tensors="pt",
                max_length=256,
                truncation=True,
                padding='max_length'
            ).to(self.device)
            
            logits = self.thought_net(inputs)
            thought_ids = torch.argmax(logits, dim=-1)
            return self.tokenizer.decode(thought_ids[0], skip_special_tokens=True)

    def _refine_thought(self, thought, context):
      prompt = f"Context:\n{context}\nRefine the following internal thought to make it more relevant and coherent with the conversation:\n{thought}\nRefined Thought:"
      inputs = self.tokenizer.encode(
          prompt,
          return_tensors="pt",
          max_length=512,
          truncation=True
      ).to(self.device)
      
      outputs = self.model.generate(
          inputs,
          max_new_tokens=50,
          temperature=0.7,
          do_sample=True
      )
      
      refined_thought = self.tokenizer.decode(outputs[0], skip_special_tokens=True).split("Refined Thought:")[-1].strip()
      
      # Ensure refined thought isn't empty or repetitive
      if not refined_thought or refined_thought.lower() == thought.lower():
          refined_thought = thought  # Default to the original thought if the refinement is not useful
      
      return refined_thought


    def train_thought_network(self, epochs=3):
        self.thought_net.train()
        for epoch in range(epochs):
            total_loss = 0
            for conv, thought in self.thought_loader:
                self.thought_optim.zero_grad()
                
                conv = conv.to(self.device)
                thought = thought.to(self.device)
                
                outputs = self.thought_net(conv)
                loss = self.thought_criterion(
                    outputs.view(-1, outputs.size(-1)),
                    thought.view(-1)
                )
                
                loss.backward()
                self.thought_optim.step()
                total_loss += loss.item()
            
            print(f"Thought Network Epoch {epoch+1} | Loss: {total_loss/len(self.thought_loader):.4f}")

    def chat(self):
        print("Sophia: Hello! I'm Sophia with neural self-thinking. Type 'train' to enhance my thinking!")
        while True:
            try:
                user_input = input("\nYou: ")
                if user_input.lower() == 'exit':
                    break
                elif user_input.lower() == 'train':
                    print("\nSophia: Engaging in deep learning...")
                    self.train_thought_network()
                    print("Sophia: My thinking has improved!")
                    continue
                
                response = self.generate_response(user_input)
                print(f"\nSophia: {response}")
                print(f"\n[Internal Thought] {self.thoughts[-1] if self.thoughts else 'Processing...'}")
                
            except Exception as e:
                print(f"\nSophia: Let's try that again. Could you rephrase?")
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    ai = ConversationAI()
    ai.chat()
