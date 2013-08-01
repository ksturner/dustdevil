from os import path

settings = dict(
    port = 5001,
    db_name = "",
    db_uri  = "",
    db_user = "",
    db_pass = "",
    login_url="/auth/login",
    static_path = path.join(path.dirname(__file__), "app/static"),
    template_path = path.join(path.dirname(__file__), "app/templates"),
    cookie_secret = "ENTER IN YOUR OWN UNIQUE VALUE HERE",
    debug = False,
    debug_pdb = False,
)
try:
    from settings_prod import settings as settings_prod
    settings.update(settings_prod)
except ImportError:
    try:
        from settings_dev import settings as settings_dev
        settings.update(settings_dev)
    except ImportError:
        pass

