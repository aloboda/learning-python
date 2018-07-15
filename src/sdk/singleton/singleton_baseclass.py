class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


class Logger(Singleton):
    pass


logger = Logger()
logger2 = Logger()

print('logger == logger2: {}'.format(logger == logger2))
