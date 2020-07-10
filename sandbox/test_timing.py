from sandbox.timing import tm


@tm
def a(b):
    for i in range(b):
        print(i)
    else:
        print('Done!')


a(10)
a(100)
a(-5)
