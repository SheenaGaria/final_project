# pylint: disable=import-error
"""
Flask server for Emotion Detection web application.

This module deploys a web-based interface that allows users
to analyze emotions in text using the EmotionDetection package.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route("/")
def index():
    """
    Render the home page of the application.

    Returns:
        HTML template for the index page.
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def emotion_detect():
    """
    Analyze emotions from user-provided text.

    Returns:
        A formatted string containing emotion scores and
        the dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
