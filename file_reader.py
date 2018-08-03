import os


class FileReader:
    def __init__(self, path):
        self._path = path

    def read(self):
        try:
            wifh open(self._path, 'r') as f:
                return f.read()
        except IOError:
            return ""
