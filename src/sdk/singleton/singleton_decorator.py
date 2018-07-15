def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Logger:
    pass

@singleton
class Logger2:
    pass


logger = Logger()
logger2 = Logger()

print('logger == logger2: {}'.format(logger == logger2))
