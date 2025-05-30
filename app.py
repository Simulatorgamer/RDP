from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    tts = gTTS(text=text, lang='en')
    output_path = "static/output.mp3"
    tts.save(output_path)
    return "success"

@app.route('/audio')
def audio():
    return send_file("static/output.mp3", mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(debug=True)