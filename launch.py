#!/usr/bin/env python
import argparse

#from optparse import OptionParser

import logging
import os
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web

from settings import settings

import app
from app.views.viewlib import route


def setup_parser():
    ''' Setup our command line options and required arguments. '''
    p = argparse.ArgumentParser(description='Tornado Application Launcher',
                                epilog='')
    # Options
    p.add_argument('--loglevel', type=str,
                   help='one of: DEBUG, INFO, WARNING, ERROR, CRITICAL',
                   default='INFO')
    p.add_argument('-r', '--routes', action='store_true', dest='routes',
                   help='Prints list of known routes and then exits.')
    p.add_argument('-p', '--port', type=int, dest='port',
                   default=settings['port'],
                   help='Override default port of %s' % settings['port'])
    return p


def setup_logger(args):
    ''' Set the loglevel and intialize our logger. '''
    numeric_level = getattr(logging, args.loglevel, None)
    fmt = '%(levelname)s %(filename)s: %(message)s'
    logging.basicConfig(level=numeric_level, format=fmt)
    logging.info("Using loglevel: {0}; use --loglevel to change".format(args.loglevel))


def start_instance(settings):
    http_server = tornado.httpserver.HTTPServer(app.setup_app(settings))
    http_server.listen(settings['port'])
    try: tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt: pass


if __name__ == "__main__":
    args = setup_parser().parse_args()
    setup_logger(args)

    if args.routes:
        L = max( len(r) for r,c in routes ) # len of longest path
        fmt_ = "    %%-%ds => %%s" % L
        for r,c in  routes:
            # NOTE: we don't use logging here b/c it's requested output
            print fmt_ % (r, ".".join((c.__module__, c.__name__)))
        sys.exit(0)
    else:
        settings['port'] = args.port
        logging.info("starting Tornado on port %s", settings['port'])
        start_instance(settings)
