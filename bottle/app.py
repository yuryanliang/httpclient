from bottle import route, run


@route('/')
def index():
    return '<h1> Hello World! </h1>'


if __name__ == '__main__':
    run()
