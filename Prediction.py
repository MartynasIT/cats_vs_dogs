import cv2
import numpy as np


class Prediction:

    def __init__(self, model):
        self.model = model

    def shape_image(self, file):
        image = cv2.imread(file)
        image = cv2.resize(image, (64, 64))
        image = np.reshape(image, [1, 64, 64, 3])
        return image

    def predict(self, image):
        recognized_val = self.model.predict_classes(image)
        prediction = ''
        if recognized_val == 0:
            prediction = 'cat'
        elif recognized_val == 1:
            prediction = 'dog'
        else:
            # does not matter since all of these models return either cat or dog
            # but added for sake of better models
            prediction = 'unknown_class'
        return prediction
