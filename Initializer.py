from Loader import Loader
from Prediction import Prediction
from Utilities import Helpers


class Initializer:

    def __init__(self, model_file, directory):
        self.model_file = model_file
        self.directory = directory
        self.model = None
        self.set_once()

    def set_once(self):
        self.model = Loader(self.model_file).load_model()
        prediction_object = Prediction(self.model)
        self.run(prediction_object)

    def run(self, prediction_object):
        helper = Helpers(path=self.directory)
        images = helper.scan_files()
        for image in images:
            helper = Helpers(path=image)
            extension = helper.get_file_extension()
            if 'jpg' in extension or 'png' in extension:
                resized_image = prediction_object.shape_image(image)
                answer = prediction_object.predict(resized_image)
                print(helper.get_filename(), '|', answer)
            else:
                print(helper.get_filename(), '|', 'unsupported_file')


if __name__ == '__main__':
    print('Program has started!')
    directory = input("Enter directory: ")
    helper = Helpers(path=None)
    print(helper.get_current_dir())
    model_file = helper.get_current_dir() + '/dogvscat.h5'
    del helper
    Initializer(model_file, directory)
