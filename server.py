"""
Server for Emotion Detection using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

def dominant_emotion(emotion_scores):
    """Return the emotion with the highest score from the dictionary."""
    # If emotion_scores is empty, max() will raise ValueError
    key = max(emotion_scores, key=emotion_scores.get)
    return key, emotion_scores[key]

@app.route("/emotionDetector", methods=["GET", "POST"])
def emo_detect():
    """Route for detecting dominant emotion from input text."""
    text = request.args.get('textToAnalyze') or request.form.get('textToAnalyze')
    
    # Check for blank text input
    if not text or text.strip() == "":
        return "Text field is blank. Please try again."
    
    scores = emotion_detector(text)
    
    # Check if response has error or is invalid
    if not scores or 'error' in scores:
        return "Invalid text. Please try again."
    
    # Attempt to determine dominant emotion
    try:
        emotion, score = dominant_emotion(scores)
    except ValueError:
        return "Invalid text. Please try again."
    
    # If dominant emotion is None or empty
    if not emotion:
        return "Invalid text. Please try again."
    
    # Return dominant emotion and the entire raw emotion scores dictionary
    return (
        f"The dominant emotion is {emotion}, with a score of {score}.<br>"
        f"Raw response: {scores}"
    )

@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
