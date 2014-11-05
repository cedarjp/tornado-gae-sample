# set encoding=utf-8
import os
from tornado.ioloop import IOLoop
import tornado.wsgi
import tornado.web
import tornado.options
from tornado.options import define, options
from tornado.util import import_object
 
 
define("port", default=8888, help="run on the given port", type=int)
 
 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/', import_object('handler.HelloHandler')),
                ]
        settings = dict(
                template_path = os.path.join(os.path.dirname(__file__), "templates"),
                )
        tornado.web.Application.__init__(self, handlers, **settings)
 
def make_app():
    return Application()

wsgi_app = tornado.wsgi.WSGIAdapter(make_app())

def main():
    app = make_app()
    app.listen(options.port)
    IOLoop.current().start()
 
if __name__ == '__main__':
    main()
