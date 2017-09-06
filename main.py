#!/usr/local/bin/python
# coding:utf8
import tornado.ioloop
import tornado.web
import json
from pymongo import MongoClient

client = MongoClient()
db = client['home']


class TestHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(TestHandler, self).__init__(application, request, **kwargs)
        self.tbl = db['events']

    def data_received(self, chunk):
        pass

    def get(self):
        print("get request")
        self.write({"str": "hello tornado"})

    def post(self):
        body = json.loads(self.request.body)
        print(type(body))
        self.tbl.insert_one(body)
        self.write({"echo:": str(body)})


def make_app():
    return tornado.web.Application([
        (r"/", TestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(3003)
    tornado.ioloop.IOLoop.current().start()
