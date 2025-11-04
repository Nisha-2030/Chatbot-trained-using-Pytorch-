import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ChatbotAssistant:
    def __init__(self, intents_file):
        with open(intents_file) as f:
            self.intents = json.load(f)

        self.patterns = []
        self.responses = []
        self.tags = []

        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                self.patterns.append(pattern)
                self.responses.append(intent["responses"])
                self.tags.append(intent["tag"])

        # Vectorizer
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.patterns)

    def load_model(self, path):
        # If no DL model, just keep it for compatibility
        return

    def process_message(self, message):
        if not message.strip():
            return "Please type something."

        # Convert user message
        user_vec = self.vectorizer.transform([message])
        similarities = cosine_similarity(user_vec, self.X)

        best_match = similarities.argmax()
        best_score = similarities[0][best_match]

        # 👇 Fallback threshold
        threshold = 0.35
        if best_score < threshold:
            return "Sorry, I can't understand. Can you please rephrase?"

        return random.choice(self.responses[best_match])
