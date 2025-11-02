#  Voice Assistant

A beautiful voice-controlled assistant with an ocean-themed interface, powered by Flask, Google Gemini AI, and speech recognition.

![Ocean Voice Assistant](https://img.shields.io/badge/Voice-Assistant-00bcd4?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)

## ✨ Features

- 🎤 *Voice Recognition* - Speak naturally to interact with the assistant
- 🌊 *Beautiful UI* - Animated waves and glowing sphere interface
- 🤖 *AI-Powered* - Integration with Google Gemini for intelligent responses
- 🔊 *Text-to-Speech* - Natural voice responses
- 🌐 *Web Control* - Open websites and perform web searches
- ⏰ *Time & Date* - Get current time and date information

## 🎯 Commands

| Command | Action |
|---------|--------|
| "What time is it?" | Get current time |
| "What's the date?" | Get today's date |
| "Open Google" | Opens Google in browser |
| "Open YouTube" | Opens YouTube in browser |
| "Search [query] on Google" | Search Google |
| "Search [query] on YouTube" | Search YouTube |
| "Open [website]" | Open any website |
| "Ask Gemini [question]" | Query Google Gemini AI |
| "Stop" / "Exit" / "Bye" | Exit assistant |

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Edge)
- Microphone access

### Step 1: Clone the Repository

bash
git clone https://github.com/yourusername/voiceassistant.git
cd voiceassistant


### Step 2: Install Dependencies

bash
pip install flask pyttsx3 google-generativeai


### Step 3: Configure API Key

1. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Open the Python backend file
3. Replace the API key:

python
genai.configure(api_key="YOUR_API_KEY_HERE")


## 🏃 Running the Application

### Step 1: Start the Backend Server

bash
python app.py


You should see:

🚀 Backend server running on http://localhost:5000


### Step 2: Open the Frontend

1. Open index.html in your web browser
2. Allow microphone access when prompted
3. Click the *🎤 Speak* button and start talking!

## 📁 Project Structure


voice-assistant/
├── index.html          # Frontend UI with theme
├── backend.py             # Flask backend server
└── README.md          # This file


## 🔧 Configuration

### Change Voice Settings

Edit in backend.py:

python
engine.setProperty('rate', 170)      # Speech speed (150-200)
engine.setProperty('volume', 1.0)    # Volume (0.0-1.0)
engine.setProperty('voice', voices[1].id)  # voices[0] = Male, voices[1] = Female


### Customize UI Colors

Edit in index.html <style> section:

css
background: linear-gradient(180deg, #001f3f, #0074D9);  /* Background gradient */
background: radial-gradient(circle, #00eaff, #0077ff);  /* Sphere colors */


## 🛠 Troubleshooting

### Microphone Not Working
- Ensure microphone permissions are granted in browser
- Check browser console for errors (F12)
- Try using https:// instead of file:// protocol

### Backend Connection Failed
- Verify Flask server is running on port 5000
- Check firewall settings
- Look for CORS errors in browser console

### Voice Recognition Not Starting
- Only works in modern browsers (Chrome recommended)
- Requires HTTPS or localhost
- Check browser compatibility for Web Speech API

### pyttsx3 Not Speaking
bash
# On Linux, install espeak
sudo apt-get install espeak

# On macOS, use built-in voices
# On Windows, uses SAPI5 (built-in)


## 🌐 Browser Compatibility

| Browser | Speech Recognition | Text-to-Speech |
|---------|-------------------|----------------|
| Chromev |          ✅        |      ✅       |
| Edge vvv|          ✅        |      ✅       |
| Firefox |      ⚠ Limited     |      ✅       |
| Safari v|      ⚠ Limited     |      ✅       |

## 📝 API Reference

### Backend Endpoint

*POST* /process

Request:
json
{
  "text": "what time is it"
}


Response:
json
{
  "reply": "The time is 3:45 PM"
}


## 🎨 Customization Ideas

- Add more voice commands
- Integrate with smart home devices
- Add weather information
- Create custom themes
- Add chat history export
- Implement wake word detection


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 💡 Future Enhancements

- [ ] Multi-language support
- [ ] Custom wake word
- [ ] Offline mode
- [ ] Mobile app version
- [ ] Voice training for better accuracy
- [ ] Integration with calendar/reminders
- [ ] Music playback control

## 👤 Author

Project Link: [https://github.com/sanskruti123987/voiceassistant](https://github.com/sanskruti123987/voiceassistant)

##  Acknowledgments

- Google Gemini AI for intelligent responses
- Flask for the backend framework
- Web Speech API for voice recognition
- pyttsx3 for text-to-speech

---

⭐ If you found this project helpful, please give it a star!