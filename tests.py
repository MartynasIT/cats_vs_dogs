import Utilities as util
from Initializer import Initializer


def test_animals(answers, dir, mode):
    total_files = util.count_files(dir)
    mode_elements = 0
    for answer in answers:
        if mode in answer:
            mode_elements += 1

    assert mode_elements == total_files, 'There are {0} {1} but predicted only {2}'. \
        format(mode_elements, mode, total_files)
    print('{0} predicted with 100% accuracy'.format(mode))


print('Tests have started!')
model_file = util.get_current_dir() + '/dogvscat.h5'
directory = util.get_current_dir() + '/tests/dogs'
obj = Initializer(model_file, directory)
answers_dogs = obj.get_answers()
test_animals(answers_dogs, directory, 'dog')

directory = util.get_current_dir() + '/tests/cats'
obj = Initializer(model_file, directory)
answers_cats = obj.get_answers()
test_animals(answers_cats, directory, 'cat')

directory = util.get_current_dir() + '/tests/unsupported'
obj = Initializer(model_file, directory)
answers_unsupported = obj.get_answers()
test_animals(answers_unsupported, directory, 'unsupported_file')