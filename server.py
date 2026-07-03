"""
Emotion Detection Web Application

This module implements a Flask-based web application that provides
emotion analysis for user-submitted text. It exposes two routes:

/emotionDetector
Accepts a query parameter 'textToAnalyze', processes the input using
the emotion_detector function, and returns a formatted response
containing emotion scores (anger, disgust, fear, joy, sadness) along
with the dominant emotion.
/
Renders the main user interface via the 'index.html' template.

Dependencies:
- Flask: For handling HTTP requests and rendering templates.
- EmotionDetection.emotion_detection.emotion_detector:
Custom function for performing emotion analysis.

Usage:
Run the application and navigate to the root URL to access the UI,
or call the /emotionDetector endpoint with appropriate query parameters.

Example:
/emotionDetector?textToAnalyze=I am very happy today

Author:
[Maithri Hegde]

"""
from flask import request, Flask, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion detector')

@app.route('/emotionDetector')
def emotions_detector():
    """
    Analyze the emotional tone of a given text input.

    This endpoint retrieves a text string from the query parameter
    'textToAnalyze', processes it using the emotion_detector function,
    and returns a formatted string containing the detected emotions
    and the dominant emotion.

    Query Parameters:
        textToAnalyze (str): The input text to analyze.

    Returns:
        str: A formatted message containing emotion scores (anger, disgust,
        fear, joy, sadness) and the dominant emotion. If the input is invalid,
        returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is \'anger\': {response['anger']}, \'disgust\': {response['disgust']}, \'fear\': {response['fear']}, \'joy\': {response['joy']} and \'sadness\': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route('/')
def render_index():
    """
    Render the homepage of the application.

    This endpoint serves the main HTML page for the Emotion Detector app.

    Returns:
        str: Rendered HTML content of the 'index.html' template.
    """
    return render_template('index.html')

if __name__ == 'main':
    app.run(host='0.0.0.0',port=5000)
