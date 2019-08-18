def f():
    global s
    print("inside f before change:", s)
    # This program will NOT show error
    # if we comment below line.
    s = "changed"
    print("inside f after change:", s)


if __name__ == '__main__':
    s = "hello word"
    f()
    print("global s:", s)
