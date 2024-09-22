from keras.models import load_model
from keras.preprocessing import image
import time
time.clock = time.time
import numpy as np

class Node:
    def __init__(self, corr, probs):
        self.cor = corr
        self.probs = probs  # List of probabilities for each class

def predict_image(filepath):
    """Load the image and make a prediction."""
    model = load_model(r"MainWebsite/skincancerml.h5", compile=False)
    img = image.load_img(filepath, target_size=(180, 180))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)
    prediction = [1-float(pred[0]), float(pred[0])]
    return Node(0.85, prediction)