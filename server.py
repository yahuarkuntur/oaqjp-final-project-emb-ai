'''
    Deployment of the Flask app.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/")
def index_page():
    '''
        Renders the index page.
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    '''
        Analyzes the submited text and returns emotions data.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_response = emotion_detector(text_to_analyze)

    if emotion_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    emotion_keys = ("anger", "disgust", "fear", "joy", "sadness")

    emotion_key_values = []
    response_text = "For the given statement, the system response is "

    for key in emotion_keys:
        emotion_key_values.append(f"'{key}': {emotion_response[key]}")

    last_emotion_key_value = emotion_key_values.pop()
    dominant_emotion = emotion_response['dominant_emotion']

    response_text += ", ".join(emotion_key_values) + " and " + last_emotion_key_value

    response_text += f". The dominant emotion is <strong>{dominant_emotion}</strong>."

    return response_text


if __name__ == '__main__':
    app.run(port=5000, debug=True)
