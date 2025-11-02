# Voice Assistant #

Hey there 👋!  
Meet your personal **Voice Assistant** — built with **Flask + HTML/CSS/JS**, this smart bot listens 🎧, understands 🧠, and talks back 🗣️ and also uses **Google Gemini AI** for more advanced answers.
Whether you want to open YouTube, check the time, or chat about anything, it’s ready to help — hands-free!

-----------------------------------------------------------------------------------------------------------------------------------------------

# Features #

✨ Smooth, responsive, and fun to use — all powered by your voice!  

|        💡 Feature        |          🧩 Description          |
----------------------------------------------------------------
|   🎙️ Voice Recognition   | Speak naturally — no need to type |
|     🤖 Gemini AI Chat    | Get real, intelligent answers     |
|    🌐 Web Navigation     | Opens Google, YouTube, and more   |
|     🔍 Smart Search      | Searches the web with one command |
|      🕒 Time & Date      | Tells you the current time/date   |
|     🗣️ Speech Output     | Talks back using realistic voices |
|      💫 Animated UI      | Glowing chat bubble interface     |

-----------------------------------------------------------------------------------------------------------------------------------------------

# Tech Stack #

|   🧩 Layer   |               💻 Technology               |
-------------------------------------------------------------
|    Backend    | Flask (Python)                            |
|    Frontend   | HTML, CSS, JavaScript                     |
|    AI Model   | Google Gemini API                         |
|  Voice Engine | pyttsx3 + Web Speech API                  |
|    Helpers    | flask-cors, datetime, urllib, webbrowser  |

-----------------------------------------------------------------------------------------------------------------------------------------------

# Project Structure #

va_final/
│
├── templates/
│   └── index.html       # Frontend HTML (UI)
│
├── backend.py           #  Main voice assistant backend (Flask + Gemini(only for task asked for) + pyttsx3)
├── audio_api.py         #  Mini API layer (connects frontend to backend.py)
│
├── requirements.txt     #  Python dependencies
└── README.md            #  Project documentation

