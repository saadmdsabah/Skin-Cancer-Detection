import cv2
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

class Node:
    def __init__(self, corr, probs):
        self.cor = corr
        self.probs = probs

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def model_prediction_mobilenet(image_path):
    model = load_model('MainWebsite/MobileNetV2.h5')
    input_img = preprocess_image(image_path)
    predictions = model.predict(input_img)
    return Node(0.77, predictions[0])

