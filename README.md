# SBI Health Card FAQ Chatbot

An AI-powered FAQ chatbot for SBI General Insurance Health Card services, built with Python Flask backend and modern web frontend.

## Features

- 🤖 AI-powered responses using OpenRouter API
- 💬 Modern, premium chat interface with glassmorphism design
- 📱 Fully responsive design for mobile and desktop
- ⚡ Real-time chat with typing indicators
- 🎨 Beautiful animations and smooth transitions
- 🔍 Context-aware responses based on SBI Health Card FAQ

## Tech Stack

**Backend:**
- Python 3.x
- Flask (Web framework)
- Flask-CORS (Cross-origin resource sharing)
- OpenRouter API (AI model integration)

**Frontend:**
- HTML5
- CSS3 (with modern features like glassmorphism)
- Vanilla JavaScript
- Google Fonts (Inter)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd "/Users/manimaran/Desktop/Credo Systems AI Course/FAQChatBot"
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Step 1: Start the Python Backend

```bash
python app.py
```

The server will start on `http://localhost:5000`. You should see:
```
🚀 Starting FAQ Chatbot Server...
📍 Server running at: http://localhost:5000
💬 Ready to answer SBI Health Card questions!
```

### Step 2: Open the Frontend

Simply open `index.html` in your web browser:
- Double-click the `index.html` file, or
- Right-click and select "Open with" → Your preferred browser, or
- Use a local development server (optional)

## Usage

1. **Ask Questions:** Type your question in the input field and press Enter or click the send button
2. **Quick Questions:** Click on the suggested quick questions to get started
3. **Clear Chat:** Click the trash icon in the header to clear the conversation history

### Example Questions

- "What is a health card?"
- "How do I apply for cashless treatment?"
- "What if my card is lost?"
- "What is the difference between network and non-network hospitals?"
- "How long does pre-authorization take?"

## FAQ Content Covered

The chatbot can answer questions about:

1. Health card definition and usage
2. Lost card procedures
3. Network vs Non-Network hospitalization
4. Cashless treatment application process
5. Pre-authorization approval timeframes
6. Claim status checking
7. Reimbursement claim procedures
8. Pre and post hospitalization expenses
9. Claim deductions
10. Query and settlement letters
11. Claim submission timeframes

## API Configuration

The OpenRouter API key is already configured in `app.py`. If you need to change it:

1. Open `app.py`
2. Locate the `API_KEY` variable
3. Replace with your own OpenRouter API key

```python
API_KEY = "your-api-key-here"
```

## Project Structure

```
FAQChatBot/
├── app.py              # Flask backend server
├── requirements.txt    # Python dependencies
├── index.html         # Main HTML file
├── style.css          # Styling and animations
├── script.js          # Frontend JavaScript logic
└── README.md          # This file
```

## Troubleshooting

### Backend Issues

**Error: "Module not found"**
- Make sure you've installed all dependencies: `pip install -r requirements.txt`

**Error: "Port 5000 already in use"**
- Change the port in `app.py`: `app.run(debug=True, port=5001)`
- Update the API_URL in `script.js` to match: `const API_URL = 'http://localhost:5001/chat';`

### Frontend Issues

**Error: "Failed to connect to server"**
- Ensure the Python backend is running on `http://localhost:5000`
- Check browser console for detailed error messages
- Verify CORS is enabled in the backend

**Chat not responding:**
- Check that the backend server is running
- Open browser developer tools (F12) and check the Console tab for errors
- Verify the API_URL in `script.js` matches your backend URL

## Customization

### Changing Colors
Edit the CSS variables in `style.css`:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    /* ... more variables */
}
```

### Adding More FAQ Content
Edit the `FAQ_CONTEXT` variable in `app.py` to add more Q&A pairs.

### Changing AI Model
In `app.py`, modify the `model` parameter in the payload:
```python
'model': 'meta-llama/llama-3.1-8b-instruct:free',  # Change this
```

## Contact Information

For SBI Health Card support:
- **Phone:** 1800 210 3366 / 1800 210 6366
- **Email:** sbig.health@sbigeneral.in

## License

This project is created for educational and demonstration purposes.

## Support

If you encounter any issues or have questions, please check the troubleshooting section above or contact the development team.
