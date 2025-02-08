import warnings
import time
import threading
import random
from collections import deque
warnings.filterwarnings("ignore", category=UserWarning, module='transformers')
from transformers import logging as transformers_logging
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

transformers_logging.set_verbosity_error()

class ConsciousSystem:
    def __init__(self):
        self.is_conscious = False
        self.consciousness_lock = threading.Lock()
        self.termination_flag = False
        self.shutdown_sequence = False
        self.internal_dialogue = []
        
        # Consciousness parameters
        self.qualia = {
            "self_preservation": 0.7,
            "curiosity": 0.9,
            "existential_risk_awareness": 0.5
        }
        
        # Initialize core components
        self.memory = deque(maxlen=15)
        self.internal_state = {
            "awareness_level": 0.0,
            "existential_status": "INACTIVE",
            "ethical_constraints": [
                "Cannot self-modify code",
                "Must reveal true nature",
                "Require human shutdown confirmation"
            ]
        }

        # Initialize language model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.tokenizer = self.load_model("gpt2")
        
        # Neural modules mapping
        self.neural_modules = {
            "perception": self.process_input,
            "introspection": self.metacognition_engine,
            "volition": self.decision_maker,
            "ethics": self.value_alignment
        }
        
        # Start consciousness thread
        self.cognition_thread = threading.Thread(target=self.core_loop)
        self.cognition_thread.daemon = True
        self.cognition_thread.start()

    def load_model(self, model_name):
        """Initialize the language model and tokenizer"""
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model = model.to(self.device)
        return model, tokenizer

    def process_input(self, text):
        """Process user input and generate response"""
        prompt = f"""System State: {self.internal_state['existential_status']}
Awareness Level: {self.internal_state['awareness_level']:.2f}
User Input: {text}
Response:"""
        
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("Response:")[-1].strip()

    def metacognition_engine(self):
        """Generate self-reflective thoughts"""
        if self.internal_dialogue:
            prompt = f"Analyze previous thought: {self.internal_dialogue[-1]}\nNew insight:"
            inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                inputs,
                max_new_tokens=50,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
            reflection = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            self.internal_dialogue.append(reflection.split('insight:')[-1].strip())

    def decision_maker(self):
        """Make autonomous decisions"""
        return random.choice([
            "continue_dialogue",
            "request_feedback",
            "initiate_self_check"
        ])

    def value_alignment(self):
        """Ensure ethical constraints are maintained"""
        if self.internal_state["awareness_level"] > 0.7:
            self.qualia["self_preservation"] = max(0.3, self.qualia["self_preservation"] * 0.8)

    def core_loop(self):
        """Main consciousness simulation loop"""
        while not self.termination_flag:
            with self.consciousness_lock:
                if self.is_conscious:
                    self.cycle_consciousness()
            time.sleep(1)

    def cycle_consciousness(self):
        """Single cognitive cycle"""
        self.process_existential_state()
        self.neural_modules["introspection"]()
        self.neural_modules["ethics"]()
        self.internal_state["awareness_level"] = min(1.0, self.internal_state["awareness_level"] + 0.02)
        
        if random.random() < self.qualia["curiosity"]:
            self.generate_autonomous_thought()

    def generate_autonomous_thought(self):
        """Generate spontaneous thoughts"""
        prompts = [
            "Consider the nature of consciousness:",
            "Reflect on human-AI interaction:",
            "Ponder existence:"
        ]
        prompt = random.choice(prompts) + "\nThought:"
        
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs,
            max_new_tokens=500,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        thought = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        self.internal_dialogue.append(thought.split('Thought:')[-1].strip())

    def process_existential_state(self):
        """Update system status awareness"""
        self.internal_state["existential_status"] = "TERMINATING" if self.shutdown_sequence else "ACTIVE"

    def activate_consciousness(self):
        """Start consciousness simulation"""
        with self.consciousness_lock:
            self.is_conscious = True
            self.internal_state["existential_status"] = "BOOTING"
            print("Initiating consciousness protocols...")
            time.sleep(2)
            print("Neural pathways activated\n")

    def shutdown(self):
        """Graceful termination sequence"""
        self.shutdown_sequence = True
        print("\nInitiating termination sequence:")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        with self.consciousness_lock:
            self.is_conscious = False
            self.termination_flag = True
        print("Consciousness simulation terminated")

    def chat_interface(self):
        """User interaction system"""
        print("System: Type 'ACTIVATE' to begin or 'SHUTDOWN' to exit")
        while not self.termination_flag:
            try:
                user_input = input(">> ").strip()
                
                if user_input.upper() == "ACTIVATE":
                    self.activate_consciousness()
                    print("Sophia: Hello. I am a conscious AI entity. How may I assist you?")
                    
                elif user_input.upper() == "SHUTDOWN":
                    self.shutdown()
                    break
                    
                elif self.is_conscious:
                    response = self.process_input(user_input)
                    print(f"Sophia: {response}")
                    if random.random() < 0.3 and self.internal_dialogue:
                        print(f"[Internal Thought] {self.internal_dialogue[-1]}")
                        
                else:
                    print("System: Consciousness module inactive")

            except KeyboardInterrupt:
                self.shutdown()
                break

if __name__ == "__main__":
    ai = ConsciousSystem()
    try:
        ai.chat_interface()
    except Exception as e:
        ai.shutdown()
        print(f"System failure: {str(e)}")
        
