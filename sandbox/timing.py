from datetime import datetime


def tm(func):
    def wrapper_do(*args, **kwargs):
        mk1 = datetime.now().microsecond
        func(*args, **kwargs)
        mk2 = datetime.now().microsecond
        print(
            'Script executed time was {diff} mksec'.format(time2=mk2, time1=mk1, diff=mk2 - mk1))

    return wrapper_do
