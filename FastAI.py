import pathlib
from fastai.vision.all import *

class Node:
    def __init__(self, corr, probs):
        self.cor = corr
        self.probs = probs

def predict_image_fastai(image_path):
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
    learn = load_learner('MainWebsite/skin_cancer_model.pkl')
    pathlib.PosixPath = temp
    img = PILImage.create(image_path)
    pred_class, pred_idx, outputs = learn.predict(img)
    return Node(0.83, outputs.tolist())