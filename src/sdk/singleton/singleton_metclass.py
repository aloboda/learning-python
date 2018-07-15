class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


logger = Logger()
logger2 = Logger()

print('logger == logger2: {}'.format(logger == logger2))
