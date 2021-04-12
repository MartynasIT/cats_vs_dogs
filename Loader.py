import keras


class Loader:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        return keras.models.load_model(self.path)
