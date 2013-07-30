% Dust Devil

Dust Devil
==========

Dust Devil (DD) is a minimal Tornado template for quickly organizing a new
Tornado web application. It cleanly separates static files, templates, views
(or handlers) as well as reserving a spot for any application/database models.

You'll also find that this application uses a familiar route decorator style
that is common in other Python web frameworks.

Getting Started
---------------

You'll first want to install any python modules, such as Tornado, that you
don't already have installed. If you have `pip`, you can quickly install these
with the command:

```bash
$ pip install -r requirements.pip
```

We highly recommend that you install to a `virtualenv` so that various python
modules required by this project don't interfere with Python system modules.

Default settings are stored in `settings.py` but you are heavily encouraged to
store your custom dev, production, etc. settings in `settings_dev.py` and allow
the framework to overlay those edits automatically onto settings.py

```bash
$ cp settings_dev.py.template settings_dev.py
```

Once you have your settings specified that you want, you can quickly launch the
application using `launch.py`. The main reason for using `launch.py` versus
invoking your application directly is that loads the views cleanly so that your
routes you've specified with the route decorator are loaded properly. The
`launch.py` script also serves as a useful spot to add custom options and
arguments in the future. For full usage, type:

```bash
$ launch.py -h
```

One option to take note of is the `--routes` option which will show you the
application's mapping of routes to views just before exiting. It's quick way to
locate specific views/handlers, but also to get a quick overview of the routes
that will be used when the application is running.

*NOTE*: The order of routes is very important to take notice of, as the first
route that is satisfied will invoke the associated handler. Use of `--routes`
can help diagnose situations where multiple routes are being handled by the
same handler.

Route Decorator
---------------

The route decorator must be imported from `viewlib.py` but afterward,
decorating a handler is as simple as the following example:

```python
    @route('/some/path')
    class SomeRequestHandler(RequestHandler):
        pass
```

Remember that to see a list of all recognized routes in your application, you
can simply use:

```bash
$ launch.py --routes
```

License
-------

This falls under the same license as TornadoWeb, the Apache License, Version
2.0. Get a copy at http://www.apache.org/licenses/LICENSE-2.0.html
