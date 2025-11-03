from flask import Flask, request, jsonify                                      # server, reads incoming data from frontend, sends json response back to frontend
import your_assistant_script                                                 # import main voice assistant logic file

app = Flask(__name__)                                                     #initialises flask web app

@app.route("/process", methods=["POST"])                                        #dehines endpoint route where input is sent
def process():                                                       
    text = request.json["text"]                                                   #reads recognised speech text (from js)
    reply = your_assistant_script.process_command(text)                                # passes text here 
    return jsonify({"reply": reply})                                               # sends processed response back to frontend as json

app.run(port=5000)                                    # starts server allows html page to connect it

#serves as backend interface for voice assistant
#this is used to give response back to the user