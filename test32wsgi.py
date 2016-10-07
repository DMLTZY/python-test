from wsgiref.simple_server import make_server


def runserver(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    userurl = environ['PATH_INFO']
    return [bytes('<h1>hello {}</h1>'.format(userurl).encode())]

httpd = make_server('', 1234, runserver)
print('Web Server is starting....')
httpd.serve_forever()
