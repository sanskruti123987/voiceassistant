from flask import Flask, request, jsonify
import datetime
import webbrowser
import urllib.parse
import pyttsx3
import google.generativeai as genai
import threading
from flask_cors import CORS

# ============ CONFIGURE GEMINI ============
genai.configure(api_key="YOUR_GEMINI_API_KEY")
gemini_model = genai.GenerativeModel("gemini-flash-latest")

# ============ SETUP VOICE ENGINE ============
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    """Run pyttsx3 in a separate thread to avoid blocking Flask"""
    threading.Thread(target=lambda: (engine.say(text), engine.runAndWait())).start()

# ============ FLASK APP ============
app = Flask(__name__)
CORS(app)
@app.route("/process", methods=["POST"])
def process_command():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"reply": "Invalid request."})

    text = data["text"].lower().strip()
    print(f"🗣 Command received: {text}")

    # Default response
    response_text = "Sorry, I didn’t understand that."

    # Exit / Stop
    if any(word in text for word in ["stop", "exit", "bye"]):
        response_text = "Goodbye!"
        speak(response_text)
        return jsonify({"reply": response_text})

    # Time
    elif "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response_text = f"The time is {current_time}"

    # Date
    elif "date" in text:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response_text = f"Today’s date is {today}"

    # Open Google / YouTube
    elif "open google" in text:
        webbrowser.open("https://google.com")
        response_text = "Opening Google."
    elif "open youtube" in text:
        webbrowser.open("https://youtube.com")
        response_text = "Opening YouTube."

    # Search on Google
    elif ("search" in text or "find" in text) and ("on google" in text or "google" in text):
        query = (
            text.replace("search", "")
            .replace("find", "")
            .replace("on google", "")
            .replace("google", "")
            .strip()
        )
        if query:
            webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")
            response_text = f"Searching for {query} on Google."
        else:
            response_text = "What do you want me to search for?"

    # Search on YouTube
    elif ("search" in text or "find" in text) and ("on youtube" in text or "on yt" in text or "youtube" in text or "yt" in text):
        query = (
            text.replace("search", "")
            .replace("find", "")
            .replace("on youtube", "")
            .replace("on yt", "")
            .replace("youtube", "")
            .replace("yt", "")
            .strip()
        )
        if query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}")
            response_text = f"Searching for {query} on YouTube."
        else:
            response_text = "Please say what to search on YouTube."

    # Open other sites
    elif "open" in text:
        site = text.replace("open", "").strip()
        if "." not in site:
            site += ".com"
        url = f"https://{site}com"
        webbrowser.open(url)
        response_text = f"Opening {site}"

    # Ask Gemini
    elif "ask gemini" in text or "gemini" in text:
        query = text.replace("ask gemini", "").replace("gemini", "").strip()
        if query:
            response_text = "Let me ask Gemini..."
            try:
                gemini_response = gemini_model.generate_content(query)
                answer = gemini_response.text.strip()
                response_text = answer
            except Exception as e:
                response_text = "Sorry, I couldn’t get a response from Gemini."
        else:
            response_text = "What should I ask Gemini?"

    # Speak the response
    speak(response_text)
    return jsonify({"reply": response_text})

# ============ MAIN ============
if __name__ == "__main__":
    print("🚀 Backend server running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
