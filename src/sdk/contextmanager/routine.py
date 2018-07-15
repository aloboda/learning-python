from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename) -> None:
        self.file = filename
        self.file_channel = None

    def __enter__(self):
        print('open')
        self.file_channel = open(self.file)
        return self.file_channel

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit')
        self.file_channel.close()


@contextmanager
def open_file_generator(filename):
    file_channel= open(filename)
    try:
        yield file_channel
    finally:
        file_channel.close()


if __name__ == '__main__':
    file_test = './test.txt'
    with OpenFile(file_test) as file:
        print('with class')
        print(file.read())

    print('******')

    with open_file_generator(file_test) as file:
        print('with generator')
        print(file.read())
