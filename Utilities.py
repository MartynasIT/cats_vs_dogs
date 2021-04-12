import os
from os import listdir
from os.path import isfile, join
import numpy as np


class Helpers:
    def __init__(self, path):
        self.path = path

    def get_filename(self):
        head, tail = os.path.split(self.path)
        return tail

    def get_file_extension(self):
        return os.path.splitext(self.path)[1]

    def scan_files(self):
        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        images = np.empty(len(onlyfiles), dtype=object)
        for n in range(0, len(onlyfiles)):
            images[n] = join(self.path, onlyfiles[n])
        return images

    def get_current_dir(self):
        return os.getcwd()
