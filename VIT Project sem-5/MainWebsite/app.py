from flask import Flask, render_template, request
from chatterbot import ChatBot
from keras.models import load_model
from keras.preprocessing import image
import os
import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import numpy as np

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

@app.route("/get")
def get_bot_response():
    filenumber=int(os.listdir('MainWebsite/saved_conversations')[-1])
    filenumber=filenumber+1
    file= open('MainWebsite/saved_conversations/'+str(filenumber),"w+")
    file.write(
        'bot : Hi There! I am a medical chatbot. You can begin conversation by typing in a message and pressing enter.\n'
        )
    file.close()

    english_bot = ChatBot('Bot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'},  
                                ], trainer='chatterbot.trainers.ListTrainer')
    english_bot.set_trainer(ListTrainer)
    english_bot.initialize

    userText = request.args.get('msg')
    print(userText)
    response = str(english_bot.get_response(userText))
    appendfile=os.listdir('MainWebsite/saved_conversations')[-1]
    appendfile= open('MainWebsite/saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()
    return response

@app.route('/predict',methods = ['GET','POST'])
def upload():
    # loading the model 
    model = load_model(r"MainWebsite/skincancerml.h5",compile = False)

    if request.method=='POST':
        # image file saving
        f = request.files['image']
        basepath=os.path.dirname(__file__)
        filepath = os.path.join(basepath,'uploads',f.filename)
        f.save(filepath)

        # loading the image and doing the classification
        img = image.load_img(filepath,target_size =(180,180))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis = 0)
        pred =model.predict(x)
        if(float(pred[0]) >= 0.5):
            return "The image has been classified as not showing any signs of Cancer"
    return "The image has been classified as depicting Cancer" 

if __name__ == "__main__":
    app.run(debug=True)