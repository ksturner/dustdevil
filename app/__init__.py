import tornado.web

def setup_app(settings):
    import views
    app = tornado.web.Application(views.routes, **settings)
    return app
