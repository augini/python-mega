a = 1


def some_func():
    print(a)


def another_func():
    a = 0
    a += 1
    print(a)


some_func()
another_func()
