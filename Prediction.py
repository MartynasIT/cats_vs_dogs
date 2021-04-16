import cv2
import numpy as np


class Prediction:

    def __init__(self, model):
        self.model = model

    def shape_image(self, file):
        try:
            image = cv2.imread(file)
            image = cv2.resize(image, (64, 64))
            image = np.reshape(image, [1, 64, 64, 3])
        except cv2.error as e:
            return 'error'
        return image

    def predict(self, image):
        recognized_val = self.model.predict_classes(image)
        prediction = 'unknown_class'
        if recognized_val == 0:
            prediction = 'cat'
        elif recognized_val == 1:
            prediction = 'dog'
        return prediction
