#!/usr/bin/python
#coding:utf8
import tornado.ioloop
import tornado.web

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello tornado")

    def post(self):
        body = self.request.body
        self.write("echo:" + body)
def make_app():
    return tornado.web.Application([
        (r"/", TestHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(3003)
    tornado.ioloop.IOLoop.current().start()
