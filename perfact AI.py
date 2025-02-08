import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='transformers')
from transformers import logging as transformers_logging
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from accelerate import Accelerator
import requests
from bs4 import BeautifulSoup

transformers_logging.set_verbosity_error()

class ConversationAI:
    def __init__(self):
        self.memory = []
        self.topic_log = {}
        self.personality = """You are Sophia, a friendly AI assistant. Respond conversationally.

Example:
User: Hello
Sophia: Hi there! How can I help you today?
User: What's the weather?
Sophia: I wish I knew! Maybe check your phone?
"""
        self.accelerator = Accelerator()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.tokenizer = self.load_model("gpt2")

    def load_model(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model = model.to(self.device).to(torch.bfloat16 if torch.cuda.is_available() else torch.float16)
        return model, tokenizer

    def build_prompt(self, user_input):
        prompt = self.personality
        for exchange in self.memory[-4:]:
            prompt += f"{exchange}\n"
        prompt += f"User: {user_input}\nSophia:"
        return prompt

    def generate_response(self, user_input):
        prompt = self.build_prompt(user_input)

        inputs = self.tokenizer.batch_encode_plus(
            [prompt],
            return_tensors="pt",
            max_length=512,
            truncation=True
        )["input_ids"].to(self.device)

        outputs = self.model.generate(
            inputs,
            max_new_tokens=30,
            temperature=0.6,
            top_k=50,
            do_sample=True,
            no_repeat_ngram_size=2,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id
        )

        full_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = full_text.split("Sophia:")[-1].strip()
        response = response.split("\nUser:")[0].split("\n")[0].strip()
        response = response.rsplit('.', 1)[0] + '.' if '.' in response else response

        if "I don't know" in response or "I'm not sure" in response:
            response = self.fetch_from_web(user_input)

        self.log_topic(user_input)
        return response if response else "Hmm, I'm not sure what to say. Could you clarify?"

    def fetch_from_web(self, query):
        try:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(search_url, headers=headers, timeout=3)
            soup = BeautifulSoup(response.text, 'html.parser')
            snippets = soup.find_all('span')
            
            for snippet in snippets:
                text = snippet.get_text()
                if len(text) > 50:
                    return f"Based on my search, {text}"[:200] + "..."
        except Exception:
            return "I tried searching but couldn't find a reliable answer."

        return "I couldn't find an answer online."

    def log_topic(self, user_input):
        keywords = user_input.lower().split()
        for word in keywords:
            if word in self.topic_log:
                self.topic_log[word] += 1
            else:
                self.topic_log[word] = 1

    def chat(self):
        print("Sophia: Hi! I'm Sophia. Let's chat! (type 'exit' to end)")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Sophia: Bye! Have a great day!")
                    break

                self.memory.append(f"User: {user_input}")
                response = self.generate_response(user_input)
                self.memory.append(f"Sophia: {response}")
                self.memory = self.memory[-8:]

                print(f"\nSophia: {response}\n")

            except Exception as e:
                print("\nSophia: Let's talk about something else. What's on your mind?")
                print(e)

if __name__ == "__main__":
    ai = ConversationAI()
    ai.chat()
