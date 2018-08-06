import os
import tempfile

class File():
    def __init__(self, filename):
        self.filename = filename
        self.counter = 0

    def write(self, input_line):
        with open(self.filename, 'a') as f:
            f.write(input_line)

    def __add__(self, obj):
        new_filename = os.path.join(tempfile.gettempdir(), 'added.txt')
        with open(new_filename, 'w') as f_input:
            with open(self.filename) as f_first:
                f_input.write(f_first.read())
            with open(obj.filename) as f_second:
                f_input.write(f_second.read())
        return File(new_filename)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.filename) as f:
            content = f.readlines()
            try:
                self.counter += 1
                return content[self.counter - 1]
            except IndexError:
                self.counter = 0
                raise StopIteration

    def __str__(self):
        return self.filename

"""
file1 = File('first.txt')
file2 = File('second.txt')

print(file1 + file2)
for line in file1:
    print(line)

for line in file1:
    print(line)    

file.write('abc\n')
file.write('def\n')

print (file)"""