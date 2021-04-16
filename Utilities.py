import os
from os import listdir
from os.path import isfile, join


def get_current_dir():
    return os.getcwd()


def get_filename(path):
    head, tail = os.path.split(path)
    return tail


def get_file_extension(path):
    return os.path.splitext(path)[1]


def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])


class Helpers:
    def __init__(self, path):
        self.path = path

    def scan_files(self):
        only_files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        images = [object] * len(only_files)
        for n in range(0, len(only_files)):
            images[n] = join(self.path, only_files[n])
        return images
