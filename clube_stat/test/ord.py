

class ExitException(Exception):
    pass


try:
    a = 5/0
except ZeroDivisionError:
    raise ExitException()

