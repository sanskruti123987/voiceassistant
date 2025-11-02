from flask import Flask, request, jsonify
import your_assistant_script

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    text = request.json["text"]
    reply = your_assistant_script.process_command(text)
    return jsonify({"reply": reply})

app.run(port=5000)
