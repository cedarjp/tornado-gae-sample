# -*- coding:utf-8 -*-
import tornado.web
 
class BaseHandler(tornado.web.RequestHandler):
    pass
 
 
class HelloHandler(BaseHandler):
    def get(self):
        self.render("hello.html")
