"""Flask server for the Emotion Detector application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
      Emotion detector route function to detect users emotion from text input.
    """
    user_text = request.args.get("textToAnalyze", "")
    # Call the emotion detector
    result = emotion_detector(user_text)

    # Handle blank/invalid input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Normal output
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Render the main HTML interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
