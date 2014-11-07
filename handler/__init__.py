#    -*- coding:utf-8 -*-
from .base import BaseHandler
import tornado.gen
import tornado.httpclient
import tornado.escape


class HelloHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch('http://friendfeed-api.com/v2/feed/bret')
        json = tornado.escape.json_decode(response.body)
        self.render("hello.html", json=json, jinja2=False)

class BaseModel(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def to_dict(self):
        return dict(
                )
