#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2014,小忆机器人
All rights reserved.
摘要：
创建者：yufei
创建日期：2016/1/27
"""
import logging
import time
import signal
import sys
import os
import tornado
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define

from handler.base import auto_route_handlers
from handler.interpreter import Interpreter
from handler.interpreter import SceneInterpreter

define('port', default=8700, help='run on this port', type=int)
define('debug', default=True, help='enable debug mode')
define('project_path', default=sys.path[0], help='deploy_path')
tornado.options.parse_command_line()

class Application(tornado.web.Application):

    '''
    应用类
    '''

    def __init__(self):
        '''
        应用初始化
        '''
        settings = {
            'xsrf_cookies': False,
            'site_title': 'demo',
            'debug': options.debug,
            'static_path': os.path.join(options.project_path, 'static'),
            'template_path': os.path.join(options.project_path, 'tpl'),
        }
        handlers = auto_route_handlers
        logging.info("----> %s", handlers)
        tornado.web.Application.__init__(self, handlers, **settings)

    def log_request(self, handler):
        '''定制如何记录日志

        @handler: request handler
        '''
        status = handler.get_status()
        request_time = 1000.0 * handler.request.request_time()
        msg = '%d %s %.2f' % (
            status, handler._request_summary(), request_time)
        if status < 400:
            log_method = logging.info
        elif status < 500:
            log_method = logging.warning
        else:
            log_method = logging.error
        log_method(msg)


def shutdown(ioloop, server):
    ''' 关闭server

    :param server: tornado.httpserver.HTTPServer
    '''
    logging.info(
        "HTTP interpreter service will shutdown in %ss...", 1)
    server.stop()

    deadline = time.time() + 1

    def stop_loop():
        ''' 尝试关闭loop
        '''
        now = time.time()
        if now < deadline and (ioloop._callbacks or ioloop._timeouts):
            ioloop.add_timeout(now + 1, stop_loop)
        else:
            # 处理完现有的 callback 和 timeout 后
            ioloop.stop()
            logging.info('Shutdown!')

    stop_loop()


def main():
    ''' main 函数
    '''
    # 开启 search_engin_server
    ioloop = tornado.ioloop.IOLoop.instance()
    server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    server.listen(options.port)

    def sig_handler(sig, _):
        ''' 信号接收函数
        '''
        logging.warn("Caught signal: %s", sig)
        shutdown(ioloop, server)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    ioloop.start()


if __name__ == '__main__':
    main()

