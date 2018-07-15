def logger(function):
    print('Calling function: {function}'.format(function=function))
    return function


class CalcOperations:
    @logger
    def add(self, number1: int, number2: int) -> int:
        return number1 + number2


if __name__ == '__main__':
    # TODO:andrii.loboda:2018-06-18: makes as test
    CalcOperations().add(7, 43)
