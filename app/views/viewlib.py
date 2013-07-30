
import tornado.web
from tornado.escape import json_encode, json_decode


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("authed_user")
        return user or None

    def api_ok(self, **kwargs):
        r = {'status': 'ok'}
        r.update(kwargs)
        self.write(json_encode(r))

    def api_fail(self, **kwargs):
        r = {'status': 'fail'}
        r.update(kwargs)
        self.write(json_decode(r))

    def _handle_request_exception(self, e):
        # XXX: not sure this gets used; need to double-check
        tornado.web.RequestHandler._handle_request_exception(self,e)
        import pdb
        pdb.post_mortem()



def just_template(templ):
    ''' Generate a on-the-fly view dynamically to render template. '''
    class TemporaryGenericView(BaseHandler):
        def get(self): self.render(templ)
    return TransientGenericView


class route(object):
    '''
    Decorates RequestHandlers and builds up a list of routables handlers
    '''

    # Example
    #
    #
    # @route('/some/path')
    # class SomeRequestHandler(RequestHandler):
    #     pass
    #

    _routes = []

    def __init__(self, uri):
        self._uri = uri

    def __call__(self, _handler):
        self._routes.append((self._uri, _handler))
        return _handler

    @classmethod
    def get_routes(self):
        return self._routes



