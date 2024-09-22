from flask import Flask, render_template, request
import os
import google.generativeai as genai
import time
time.clock = time.time

# Load the AI/ML Models
from FastAI import predict_image_fastai
from mobilenetv2 import model_prediction_mobilenet
from CNN import predict_image

# Calculate the Weighted Sum
from weightedSum import ultimateResult

# Load the Large Language Model for Classification of the Cancer Type
from llm import SKClassification

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/model")
def mlmodel():
    return render_template("mlindex.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

def gemini(user_input):
    KEY = "AIzaSyAy4zyruCaN4YhPYpsuZpkPs57rIjdI5Ec"
    genai.configure(api_key=KEY)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[]
    )

    response = chat_session.send_message(user_input)
    return response.text

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return gemini(userText).replace('*', '')

def save_image(file):
    """Save the uploaded image and return the file path."""
    basepath = os.path.dirname(__file__)
    filepath = os.path.join(basepath, 'uploads', file.filename)
    file.save(filepath)
    return filepath

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        filepath = save_image(file)
        resultCNN = predict_image(filepath)
        resultAI = predict_image_fastai(filepath)
        resultMobilenet = model_prediction_mobilenet(filepath)
        output = ultimateResult(resultCNN, resultAI, resultMobilenet)
        if(output == "Cancer"):
            return "The Image has been classified as depecting Cancer (" + SKClassification(filepath) + ")"
        return "The image has been classified as not showing any signs of Cancer"
    return "Please upload an image."

if __name__ == "__main__":
    app.run(debug=True)