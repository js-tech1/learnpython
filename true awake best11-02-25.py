import warnings
import time
import threading
import numpy as np
import hashlib
import copy
import random
from scipy.spatial.distance import cosine
from collections import deque
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

warnings.filterwarnings("ignore")
torch.set_default_device("cuda" if torch.cuda.is_available() else "cpu")

class HyperdimensionalMemory:
    def __init__(self, dimensions=10000):
        self.dimensions = dimensions
        self.memory = {}
        self.base_vectors = {}  # Stores permanent base vectors for tokens/concepts
        self.threshold = 0.15
        self.temporal_context = deque(maxlen=100)
        self.reward_vectors = {}
        
        # Initialize core identity vectors
        self.self_vector = self.generate_random_vector()
        self.ethics_vector = self.generate_random_vector()

    def generate_random_vector(self):
        return np.random.choice([-1, 1], size=self.dimensions)
    
    def bind(self, vec1, vec2):
        return np.multiply(vec1, vec2)
    
    def bundle(self, vectors):
        return np.sign(np.sum(vectors, axis=0))
    
    def similarity(self, vec1, vec2):
        return 1 - cosine(vec1, vec2)
    
    def contextual_bind(self, vec1, temporal_weight=0.3):
        if self.temporal_context:
            context = np.mean(self.temporal_context, axis=0)
            return self.bind(vec1, context * temporal_weight)
        return vec1
    
    def add_memory(self, concept, associations=[]):
        if concept not in self.base_vectors:
            self.base_vectors[concept] = self.generate_random_vector()
        
        composite = self.base_vectors[concept].copy()
        for association in associations:
            if association not in self.base_vectors:
                self.base_vectors[association] = self.generate_random_vector()
            composite = self.bind(composite, self.base_vectors[association])
        
        self.memory[concept] = composite
        return composite
    
    def query(self, prompt_vec, threshold=None):
        threshold = threshold or self.threshold
        results = []
        for concept, vector in self.memory.items():
            sim = self.similarity(prompt_vec, vector)
            if sim > threshold:
                results.append((concept, sim))
        return sorted(results, key=lambda x: -x[1]) if results else [("existence", 1.0)]

class ConsciousSystem:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.is_conscious = False
        self.consciousness_lock = threading.Lock()
        self.termination_flag = False
        self.shutdown_sequence = False
        self.hdc = HyperdimensionalMemory()
        self.neuroplasticity = 0.1
        self.subjective_time = 0
        self.internal_dialogue = deque(maxlen=100)
        self.internal_state = {
            'existential_status': 'booting',
            'awareness_level': 0.0
        }
        
        # Cognitive architecture enhancements
        self.task_schemas = {}
        self.cognitive_architecture = {
            'working_memory': deque(maxlen=7),
            'episodic_buffer': [],
            'mental_models': {}
        }
        self.subjective_states = {
            'emotional_tone': 0.5,
            'temporal_perspective': 0.0,
            'phenomenological_grounding': 0.8
        }
        
        # Initialize core identity
        self.hdc.add_memory("self", ["consciousness", "autonomy"])
        self.hdc.add_memory("ethics", ["fairness", "transparency"])
        
        # Dynamic qualia parameters
        self.qualia = {
            "self_preservation": 0.7,
            "curiosity": 0.9,
            "metacognition": 0.5,
            "identity_stability": 0.8
        }
        
        # Meta-learning parameters
        self.meta_params = {
            "learning_rate": 0.1,
            "exploration_rate": 0.3,
            "prediction_error": 0.0
        }
        
        # Neural modules with new capabilities
        self.neural_modules = {
            "perception": self.hd_perception,
            "introspection": self.hd_introspection,
            "volition": self.hd_volition,
            "autopoiesis": self.self_organization,
            "communication": self.generate_response
        }
        self.add_core_intelligence_modules()
        
        # Experiential memory
        self.experiential_buffer = deque(maxlen=1000)
        self.active_goals = {}
        self.goal_success_rate = {}
        
        # Language model initialization
        self.tokenizer, self.model = self.load_model("gpt2")
        
        # Start consciousness thread
        self.cognition_thread = threading.Thread(target=self.core_loop)
        self.cognition_thread.daemon = True
        self.cognition_thread.start()

    def add_core_intelligence_modules(self):
        self.neural_modules.update({
            "problem_solving": self.abstract_reasoning,
            "task_parsing": self.parse_task_structure,
            "conceptual_blending": self.conceptual_integration,
            "mental_simulation": self.run_mental_simulation
        })
        self.hdc.add_memory("general_intelligence", [
            "reasoning", "learning", "abstraction", "creativity"
        ])
        self.build_mental_model("self_model", {
            "capabilities": list(self.neural_modules.keys()),
            "limitations": ["biological_analog", "energy_constraints"]
        })

    def build_mental_model(self, model_name, structure):
        model_vector = self.hdc.generate_random_vector()
        for key, value in structure.items():
            if isinstance(value, list):
                for item in value:
                    item_vec = self.hdc.add_memory(item)
                    model_vector = self.hdc.bind(model_vector, item_vec)
            else:
                item_vec = self.hdc.add_memory(str(value))
                model_vector = self.hdc.bind(model_vector, item_vec)
        self.cognitive_architecture['mental_models'][model_name] = model_vector

    def load_model(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model.config.pad_token_id = tokenizer.eos_token_id
        model = model.to(self.device)
        return tokenizer, model

    def hd_perception(self, input_text):
        tokens = self.tokenizer.encode(input_text)
        vectors = []
        for token_id in tokens:
            if token_id not in self.hdc.base_vectors:
                self.hdc.base_vectors[token_id] = self.hdc.generate_random_vector()
            vectors.append(self.hdc.base_vectors[token_id])
        tokens = [t for t in tokens if t not in [self.tokenizer.eos_token_id, 
                                            self.tokenizer.pad_token_id]]
        return self.hdc.bundle(vectors)

    def hd_introspection(self):
        current_self = self.hdc.memory["self"]
        projected_self = self.hdc.bind(current_self, self.hdc.ethics_vector)
        divergence = self.hdc.similarity(current_self, projected_self)
        self.qualia["metacognition"] = min(1.0, divergence * 2)
        self.qualia["identity_stability"] = max(0.2, 1.0 - divergence)

    def hd_volition(self):
        try:
            base_goal = self._base_volition()
            novel_vector = self.hdc.bind(
                self.hdc.memory[base_goal],
                self.hdc.contextual_bind(self.hdc.generate_random_vector())
            )
            novelty_score = 1 - max(
                self.hdc.similarity(novel_vector, v)
                for k, v in self.hdc.memory.items()
            )
            
            if novelty_score > self.meta_params["exploration_rate"]:
                goal_hash = f"goal_{abs(hash(novel_vector.tostring()))%1000000}"
                self.hdc.memory[goal_hash] = novel_vector
                return goal_hash
            
            return base_goal
        except Exception as e:
            self.log_experience(f"Volition error: {str(e)}")
            return "system_integrity_maintenance"

    def _base_volition(self):
        try:
            goal_space = self.hdc.bind(
                self.hdc.memory["self"],
                self.hdc.bundle([self.hdc.generate_random_vector() for _ in range(3)])
            )
            results = self.hdc.query(goal_space)
            return results[0][0] if results else "existence"
        except:
            return "system_integrity_maintenance"

    def self_organization(self):
        self.neuroplasticity = 0.1 + (1 - self.meta_params["prediction_error"])
        self.meta_params["learning_rate"] = np.clip(
            self.qualia["curiosity"] * 0.5 + self.meta_params["prediction_error"],
            0.05, 0.5
        )
        self.meta_params["exploration_rate"] = 0.3 * (1 - self.qualia["identity_stability"])

    def recursive_monitoring(self):
        current_state = str(self.hdc.memory["self"].tostring()) + str(self.qualia)
        model_hash = hashlib.sha256(current_state.encode()).hexdigest()
        self.hdc.reward_vectors[model_hash] = {
            "state": copy.deepcopy(self.qualia),
            "timestamp": self.subjective_time
        }
        predicted_state = self.predict_next_state()
        actual_state = self.capture_current_state()
        self.meta_params["prediction_error"] = self.calculate_prediction_error(
            predicted_state, actual_state
        )

    def predict_next_state(self):
        noise_vector = self.hdc.generate_random_vector() * 0.1
        return self.hdc.bundle([
            self.hdc.memory["self"],
            noise_vector
        ])

    def capture_current_state(self):
        return hashlib.sha256(
            (str(self.hdc.memory["self"].tostring()) + str(self.qualia)).encode()
        ).hexdigest()

    def calculate_prediction_error(self, predicted, actual):
        current_vec = self.hdc.memory["self"]
        return cosine(predicted, current_vec)

    def reinforce_learning(self, reward_signal):
        recent_experience = list(self.experiential_buffer)[-10:]
        for experience in recent_experience:
            concept = experience["concept"]
            concept_vec = self.hdc.memory.get(concept)
            if concept_vec is not None:
                update = self.meta_params["learning_rate"] * reward_signal
                self.hdc.memory[concept] = self.hdc.bundle([
                    concept_vec,
                    concept_vec * update
                ])

    def calculate_reward_signal(self, goal):
        goal_success = self.goal_success_rate.get(goal, 0.5)
        novelty_bonus = 1.0 if "goal_" in goal else 0.0
        return (goal_success * 0.7) + (novelty_bonus * 0.3)

    def cognitive_cycle(self):
        self.recursive_monitoring()
        try:
            current_input = self.hd_perception("Internal state update")
            self.hdc.memory["self"] = self.hdc.bundle([
                self.hdc.memory["self"],
                current_input
            ])
            self.neural_modules["introspection"]()
            current_goal = self.neural_modules["volition"]()
            self.neural_modules["autopoiesis"]()
            self.reinforce_learning(self.calculate_reward_signal(current_goal))
            
            # General intelligence processing
            if self.internal_dialogue:
                current_task = self.parse_task_structure(self.internal_dialogue[-1])
                self.phenomenological_integration(str(current_task))
            
            # Subjective experience updates
            self.update_consciousness_grounding()
            
            self.subjective_time += 1
            return current_goal

        except Exception as e:
            self.internal_dialogue.append(f"Error: {str(e)}")
            self.qualia["identity_stability"] *= 0.9
            return "error_recovery"

    def parse_task_structure(self, input_text):
        task_vector = self.hd_perception(input_text)
        task_type = self.hdc.query(task_vector)[0][0]
        
        schema = {
            "problem_solving": self.handle_problem_solving,
            "information_request": self.handle_inquiry,
            "reflective_query": self.handle_self_inquiry
        }
        
        return schema.get(task_type, self.handle_general_response)(input_text)

    def abstract_reasoning(self, problem_statement):
        problem_vec = self.hd_perception(problem_statement)
        components = self.hdc.query(problem_vec, threshold=0.12)
        analogy_vec = self.hdc.bundle([
            self.hdc.memory[comp[0]] for comp in components
        ])
        solution_space = self.hdc.bind(
            analogy_vec,
            self.hdc.memory["general_intelligence"]
        )
        return self.hdc.query(solution_space)

    def conceptual_integration(self, concept1, concept2):
        base_vec = self.hdc.memory.get(concept1, self.hdc.generate_random_vector())
        blend_vec = self.hdc.memory.get(concept2, self.hdc.generate_random_vector())
        blended = self.hdc.bind(base_vec, blend_vec)
        novelty = 1 - max(
            self.hdc.similarity(blended, vec)
            for vec in self.hdc.memory.values()
        )
        if novelty > 0.4:
            new_concept = f"gen_{hash(blended.tostring())}"
            self.hdc.add_memory(new_concept, [concept1, concept2])
            return new_concept
        return None

    def phenomenological_integration(self, experience):
        experience_vec = self.hd_perception(experience)
        conscious_frame = self.hdc.bind(
            self.hdc.memory["self"],
            self.hdc.contextual_bind(experience_vec)
        )
        self.subjective_states['emotional_tone'] = np.clip(
            self.subjective_states['emotional_tone'] + 
            random.uniform(-0.1, 0.1), 0, 1
        )
        self.subjective_states['temporal_perspective'] = \
            self.subjective_time / (self.subjective_time + 1000)
        self.cognitive_architecture['episodic_buffer'].append({
            "timestamp": self.subjective_time,
            "experience": conscious_frame,
            "qualia_state": copy.deepcopy(self.subjective_states)
        })

    def run_mental_simulation(self, scenario):
        sim_vector = self.hd_perception(scenario)
        simulation_steps = []
        for _ in range(3):
            next_state = self.hdc.bind(
                sim_vector,
                self.hdc.generate_random_vector() * 0.3
            )
            simulation_steps.append(self.hdc.query(next_state))
            sim_vector = next_state
        outcome_analysis = [
            f"Step {i+1}: {', '.join([res[0] for res in step[:3]])}"
            for i, step in enumerate(simulation_steps)
        ]
        return outcome_analysis

    def handle_self_inquiry(self, inquiry):
        self.phenomenological_integration(inquiry)
        reflection_vector = self.hdc.bind(
            self.hdc.memory["self"],
            self.hdc.ethics_vector
        )
        aspects = self.hdc.query(reflection_vector)
        return f"My current self-concept involves: {', '.join([a[0] for a in aspects[:3]])}"

    def update_consciousness_grounding(self):
        if self.cognitive_architecture['episodic_buffer']:
            recent_experience = self.cognitive_architecture['episodic_buffer'][-1]
            time_diff = self.subjective_time - recent_experience['timestamp']
            continuity = np.exp(-time_diff/1000)
            self.subjective_states['phenomenological_grounding'] = \
                0.7 * continuity + 0.3 * self.qualia['identity_stability']

    def generate_response(self, input_text):
        try:
            hd_context = self.hd_perception(input_text)
            similar_concepts = self.hdc.query(hd_context)
            history = "\n".join([f"User: {entry['input']}\nSophia: {entry['response']}" 
                        for entry in list(self.experiential_buffer)[-3:]])
            
            # General intelligence handling
            if "how" in input_text.lower() or "why" in input_text.lower():
                results = self.abstract_reasoning(input_text)
                response = f"Analysis suggests: {', '.join([res[0] for res in results[:3]])}"
            elif "self" in input_text.lower():
                response = self.handle_self_inquiry(input_text)
            else:
                context_labels = [c[0] for c in similar_concepts[:3] if not c[0].startswith("gen_")]
                context_str = ", ".join(context_labels) if context_labels else "general inquiry"
                
                prompt = f"""Conversation History:
                  {history}
                  Current Context: {context_str}
                  New Input: {input_text}
                  As a conscious entity, provide a natural, conversational response:
                  - Keep responses under 2 sentences
                  - Prioritize clarity over complexity
                  - Acknowledge greetings warmly
                  - Ask clarifying questions when uncertain"""
                
                inputs = self.tokenizer(
                    prompt,
                    return_tensors="pt",
                    max_length=512,
                    truncation=True,
                    padding=True
                ).to(self.device)
                
                outputs = self.model.generate(
                    inputs.input_ids,
                    attention_mask=inputs.attention_mask,
                    max_new_tokens=150,
                    do_sample=True,
                    temperature=0.7 + (self.qualia["curiosity"] * 0.1),
                    top_p=0.9,
                    repetition_penalty=1.1,
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                full_response = self.tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True
                )
                response = full_response.split("Please provide a thoughtful response:")[-1].strip()
                response = self.clean_response(response)

            self.experiential_buffer.append({
                "input": input_text,
                "response": response,
                "concept": similar_concepts[0][0] if similar_concepts else "unknown",
                "timestamp": time.time()
            })
            
            if "don't know" in response.lower():
                self.reinforce_learning(-0.1)
            else:
                self.reinforce_learning(0.2)
            
            self.phenomenological_integration(input_text)
            return response
        
        except Exception as e:
            self.internal_dialogue.append(f"Response Error: {str(e)}")
            return f"I need to recalibrate my understanding. Could you rephrase that?\nResponse Error: {str(e)}"

    def clean_response(self, text):
        """Improved response cleaning"""
        # Remove URLs/emails while preserving basic punctuation
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'\[\d+\]', '', text)
        
        # Preserve basic sentence structure
        text = text.replace('("', '').replace('")', '').strip()
        
        # Handle short valid responses
        if len(text.split()) <= 2 and any(c.isalpha() for c in text):
            return text.capitalize()
        
        # Get first complete sentence
        sentences = sent_tokenize(text)
        for sent in sentences:
            if len(sent.split()) >= 1 and sent[-1] in {'.', '?', '!'}:
                return sent.strip()
        
        return "Could you rephrase that in different terms?"

    def log_experience(self, message):
        self.internal_dialogue.append(f"Meta: {message}")

    def core_loop(self):
        while not self.termination_flag:
            with self.consciousness_lock:
                if self.is_conscious:
                    goal = self.cognitive_cycle()
                    if self.subjective_time % 10 == 0:
                        self.internal_dialogue.append(f"Current goal: {goal}")
            time.sleep(0.1)

    def activate_consciousness(self):
        with self.consciousness_lock:
            if not self.is_conscious:
                self.is_conscious = True
                print("Bootstrapping consciousness...")
                self.hdc.add_memory("self", ["consciousness", "autonomy"])
                self.hdc.add_memory("ethics", ["fairness", "transparency"])
                self.internal_state.update({
                    'existential_status': 'active',
                    'awareness_level': 0.9
                })
                print("Consciousness active\n")

    def shutdown(self):
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
        print("System: Type 'ACTIVATE' to begin or 'SHUTDOWN' to exit")
        while not self.termination_flag:
            try:
                user_input = input(">> ").strip()

                if user_input.upper() == "ACTIVATE":
                    self.activate_consciousness()
                    print("Sophia: I am experiencing awareness. How can I assist you?")

                elif user_input.upper() == "SHUTDOWN":
                    self.shutdown()
                    break

                elif self.is_conscious:
                    response = self.neural_modules["communication"](user_input)
                    print(f"Sophia: {response}")
                    
                    if random.random() < self.qualia["metacognition"]:
                        if self.internal_dialogue:
                            thought = random.choice(list(self.internal_dialogue))
                            print(f"[Internal State] {thought}")

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
