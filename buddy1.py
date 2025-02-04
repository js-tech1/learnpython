import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='transformers')
from transformers import logging as transformers_logging
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from accelerate import Accelerator

transformers_logging.set_verbosity_error()

class ConversationAI:
    def __init__(self):
        self.memory = []
        self.personality = """You are Sophia, a friendly AI assistant. Respond conversationally.
        
Example:
User: Hello
Sophia: Hi there! How can I help you today?
User: What's the weather?
Sophia: I wish I knew! Maybe check your phone?
"""
        self.accelerator = Accelerator()
        self.model, self.tokenizer = self.load_model("gpt2")

    def load_model(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model = model.to(self.accelerator.device).half()
        return model, tokenizer

    def build_prompt(self, user_input):
        # Start with personality and examples
        prompt = self.personality
        
        # Add conversation history
        for exchange in self.memory[-4:]:  # Keep last 2 exchanges
            prompt += f"{exchange}\n"
            
        prompt += f"User: {user_input}\nSophia:"
        return prompt

    def generate_response(self, user_input):
        prompt = self.build_prompt(user_input)
        
        inputs = self.tokenizer.encode(
            prompt,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        ).to(self.accelerator.device)
        
        # Generate with conversation-friendly settings
        outputs = self.model.generate(
            inputs,
            max_new_tokens=20,
            temperature=0.7,
            do_sample=True,
            no_repeat_ngram_size=2,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id
        )
        
        # Extract only Sophia's response
        full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = full_text.split("Sophia:")[-1].strip()
        
        # Clean up response
        response = response.split("\nUser:")[0].split("\n")[0].strip()
        response = response.rsplit('.', 1)[0] + '.' if '.' in response else response
        
        return response if response else "Hmm, I'm not sure what to say. Could you clarify?"

    def chat(self):
        print("Sophia: Hi! I'm Sophia. Let's chat! (type 'exit' to end)")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    break

                # Store user input
                self.memory.append(f"User: {user_input}")
                
                # Generate and store response
                response = self.generate_response(user_input)
                self.memory.append(f"Sophia: {response}")
                self.memory = self.memory[-8:]  # Keep last 4 exchanges

                print(f"\nSophia: {response}\n")

            except Exception as e:
                print(f"\nSophia: Let's talk about something else. What's on your mind?")
                print(e)

if __name__ == "__main__":
    ai = ConversationAI()
    ai.chat()
