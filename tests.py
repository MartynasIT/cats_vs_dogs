import os

from Loader import Loader
from Prediction import Prediction
from Utilities import Helpers


class Tests:

    def __init__(self, model_file, directory):
        self.model_file = model_file
        self.directory = directory
        self.model = None

    def set_once(self):
        self.model = Loader(self.model_file).load_model()
        prediction_object = Prediction(self.model)
        return prediction_object

    def run(self, prediction_object):
        helper = Helpers(path=self.directory)
        images = helper.scan_files()
        answers = []
        for image in images:
            helper = Helpers(path=image)
            extension = helper.get_file_extension()
            if 'jpg' in extension or 'png' in extension:
                resized_image = prediction_object.shape_image(image)
                answer = prediction_object.predict(resized_image)
                answers.append(answer)
            else:
                answers.append('unsupported_file')
        return answers

    def count_files(self):
        return len([1 for x in list(os.scandir(self.directory)) if x.is_file()])

    def count_answers(self, mode, answers):
        count = 0
        for answer in answers:
            if answer == mode:
                count += 1
        return count

    def test_dogs(self):
        predict_obj = self.set_once()
        anwers = self.run(predict_obj)
        total_dogs = self.count_files()
        counted_dogs = self.count_answers('dog', anwers)
        assert total_dogs == counted_dogs, 'There are {0} dogs but predicted only {1}'.format(total_dogs, counted_dogs)
        print('Dogs predicted with 100% accuracy')

    def test_cats(self):
        predict_obj = self.set_once()
        anwers = self.run(predict_obj)
        total_cats = self.count_files()
        counted_cats = self.count_answers('cat', anwers)
        assert total_cats == counted_cats, 'There are {0} cats but predicted only {1}'.format(total_cats, counted_cats)
        print('Cats predicted with 100% accuracy')

    def test_unsupported(self):
        predict_obj = self.set_once()
        anwers = self.run(predict_obj)
        total = self.count_files()
        counted = self.count_answers('unsupported_file', anwers)
        assert total == counted, 'There are {0} bad files but predicted only {1}'.format(total, counted)
        print('Bad files predicted with 100% accuracy')


print('Tests have started!')
helper = Helpers(path=None)
model_file = helper.get_current_dir() + '/dogvscat.h5'
directory = helper.get_current_dir() + '/tests/dogs'
tests = Tests(model_file, directory)
tests.test_dogs()

directory = helper.get_current_dir() + '/tests/cats'
tests = Tests(model_file, directory)
tests.test_cats()

directory = helper.get_current_dir() + '/tests/unsupported'
del helper
tests = Tests(model_file, directory)
tests.test_unsupported()


