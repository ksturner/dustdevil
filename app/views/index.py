import tornado.web

from viewlib import BaseHandler, route


@route('/')
class IndexView(BaseHandler):
    def get(self):
        self.render('index.html')
