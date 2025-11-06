# Event Management Chatbot

This chatbot provides intelligent assistance for the College Event Management System, helping users with event information, registration details, and general queries.

## Features

- 🤖 Intelligent responses based on user queries
- 📅 Event information and scheduling
- 📝 Registration process guidance
- 🏆 Prize and accommodation details
- 📞 Contact information
- 💬 Natural conversation flow

## Quick Start

### Backend Setup

1. **Navigate to the chatbot backend directory:**
   ```bash
   cd Chatbot/backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the chatbot server:**
   ```bash
   python start_chatbot.py
   ```
   
   Or manually:
   ```bash
   python app.py
   ```

4. **Verify the server is running:**
   - The server will start on `http://127.0.0.1:5000`
   - You can test the API at `http://127.0.0.1:5000/chat`

### Frontend Integration

The chatbot is already integrated into the main Event Management System:

1. **Start the main application:**
   ```bash
   cd chatbot/frontend
   npm start
   ```

2. **Access the chatbot:**
   - Navigate to `/chatbot` in your browser
   - Or click on "Chatbot" in the navigation menu

## API Endpoints

### POST /chat
Send a message to the chatbot and receive a response.

**Request:**
```json
{
  "message": "When is the event?"
}
```

**Response:**
```json
{
  "reply": "The event will take place on March 15th, 2025 at the College Auditorium."
}
```

## Supported Queries

The chatbot can help with:

- **Greetings**: "Hi", "Hello", "Good morning"
- **Event Information**: "When is the event?", "Event details", "Venue"
- **Registration**: "How to register?", "Registration fee", "Deadline"
- **Prizes**: "Winner prizes", "Cash rewards", "Certificates"
- **Accommodation**: "Where to stay?", "Hostel facility", "Food included"
- **Event List**: "What events?", "Competitions", "Programs"
- **Rules**: "Event rules", "Dress code", "Guidelines"
- **Contact**: "Who to contact?", "Phone number", "Email"
- **Goodbye**: "Bye", "Thank you", "See you"

## Configuration

### Adding New Intents

To add new conversation patterns, edit `backend/intents.json`:

```json
{
  "tag": "new_intent",
  "patterns": ["pattern1", "pattern2", "pattern3"],
  "responses": ["Response 1", "Response 2"]
}
```

### Modifying Response Threshold

In `backend/chatbot.py`, adjust the similarity threshold:

```python
threshold = 0.35  # Lower = more lenient, Higher = more strict
```

## Troubleshooting

### Common Issues

1. **"Error connecting to backend"**
   - Ensure the chatbot server is running on port 5000
   - Check if Python dependencies are installed
   - Verify no firewall is blocking the connection

2. **Server won't start**
   - Check if port 5000 is already in use
   - Ensure all required files are present
   - Verify Python version compatibility (3.7+)

3. **Poor response quality**
   - Add more patterns to existing intents
   - Adjust the similarity threshold
   - Review and improve response text

### Dependencies

- **Backend**: Flask, Flask-CORS, scikit-learn, numpy, scipy
- **Frontend**: React, Axios, Framer Motion (already included in main app)

## Development

### File Structure
```
Chatbot/
├── backend/
│   ├── app.py              # Flask server
│   ├── chatbot.py          # Chatbot logic
│   ├── intents.json        # Training data
│   ├── requirements.txt    # Python dependencies
│   └── start_chatbot.py    # Startup script
├── frontend/               # Standalone chatbot (optional)
└── README.md              # This file
```

### Adding New Features

1. **New Response Types**: Add to `intents.json`
2. **Enhanced Logic**: Modify `chatbot.py`
3. **API Endpoints**: Extend `app.py`
4. **UI Improvements**: Update the integrated component in `sample/client/src/pages/Chatbot.js`

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the main Event Management System documentation
- Contact the development team

---

**Note**: This chatbot is designed to work seamlessly with the College Event Management System. Make sure both the main application and chatbot backend are running for full functionality.
