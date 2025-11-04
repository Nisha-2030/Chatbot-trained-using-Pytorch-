from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import ChatbotAssistant

app = Flask(__name__)
CORS(app)

bot = ChatbotAssistant('intents.json')
bot.load_model('chatbot_model.pth')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    reply = bot.process_message(data.get('message', ''))
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
