from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")  # Load once per server

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files['file']
    audio.save('temp_audio.mp3')
    result = model.transcribe('temp_audio.mp3', language='hi')  # For Hindi, set as needed
    return jsonify({'text': result["text"], 'language': result["language"]})

if __name__ == "__main__":
    app.run(port=5001)


