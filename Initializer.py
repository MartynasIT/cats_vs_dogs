import sys
from Prediction import Prediction
from Utilities import Helpers
import Utilities as util
import keras


class Initializer:
    SUPPORTED_FILES = ['.jpg', '.png']
    answer_array = []

    def __init__(self, model_file, directory):
        self.model_file = model_file
        self.directory = directory
        self.model = None
        self.set_once()
        self.prediction_object = None

    def set_once(self):
        self.load_model()
        self.prediction_object = Prediction(self.model)
        self.set_answers(self.run())

    def run(self):
        answers = []
        helper = Helpers(path=self.directory)
        images = helper.scan_files()
        for image in images:
            extension = util.get_file_extension(image)
            file_name = util.get_filename(image)
            if extension in self.SUPPORTED_FILES:
                resized_image = self.prediction_object.shape_image(image)
                if resized_image != 'error':
                    answers.append(file_name + ' |' + self.prediction_object.predict(resized_image))
                else:
                    answers.append(file_name + ' |' + 'unsupported_file')
            else:
                answers.append(file_name + ' |' + 'unsupported_file' + ' due to corruption')
        return answers

    def load_model(self):
        loaded_model = keras.models.load_model(self.model_file)
        if loaded_model:
            self.model = loaded_model
        else:
            sys.exit('Model failed')

    def set_answers(self, answers):
        self.answer_array.clear()
        self.answer_array = answers

    def get_answers(self):
        return self.answer_array


if __name__ == '__main__':
    print('Program has started!')
    directory = input("Enter directory: ")
    model_file = util.get_current_dir() + '/dogvscat.h5'
    obj = Initializer(model_file, directory)
    for answer in obj.get_answers():
        print(answer)
