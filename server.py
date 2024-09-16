from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():
    text = request.json.get("text", "")
    
    if not text:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    result = emotion_detector(text)
    
    if result.get('dominant_emotion') is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"anger: {result['anger']}, disgust: {result['disgust']}, "
        f"fear: {result['fear']}, joy: {result['joy']} and "
        f"sadness: {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    
    return jsonify({"response": response_message}), 200

if __name__ == "__main__":
    app.run(debug=True)
