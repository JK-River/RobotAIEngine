#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2014,小忆机器人
All rights reserved.
摘要：
创建者：yufei
创建日期：2016/1/27
"""
import functools
import json
import logging
import datetime
import tornado
from tornado.web import RequestHandler, MissingArgumentError, HTTPError

from utils.utils import force_utf8_new

E_SUCC = 0
E_PARAM = 1
E_INTER = 2

auto_route_handlers = []

def exception_control(func):
    ''' 异常控制装饰器
    '''
    @functools.wraps(func)
    def wrapper(self):
        ''' 装饰函数
        '''
        try:
            code, msg, body = E_SUCC, "OK", func(self)
        except (MissingArgumentError, AssertionError) as ex:
            code, msg, body = E_PARAM, str(ex), None
        except tornado.web.HTTPError:
            raise
        except Exception as ex:
            code, msg, body = E_INTER, str(ex), None
            log_msg = self.request.uri \
                if self.request.files else \
                "%s %s" % (self.request.uri, self.request.body)
            logging.error(log_msg, exc_info=True)
        self.send_json(body, code, msg)
    return wrapper


class BaseHandler(RequestHandler):
    '''基础功能封装
    '''

    def initialize(self, prefix=None):
        '''重写Handler初始化
        '''
        self.module_prefix = prefix

    def send_json(self, res, code=E_SUCC, msg=None):
        '''发送json数据, 要逐步替代send_json
        {
            'code':'状态码',
            'msg':'错误信息',
            'body':'数据内容'
        }
        '''
        result = {'code': code, 'msg': msg, 'body': res}
        result = json.dumps(result)
        self.finish(result)

    def get_argument(
            self, name, default=tornado.web.RequestHandler._ARG_DEFAULT,
            strip=True):
        '''重写以把unicode的参数都进行utf-8编码
        '''
        value = super(BaseHandler, self).get_argument(name, default, strip)
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        return value

    def process_module(self, module):
        '''
        内部路由分发
        '''
        module = module or ''
        if self.module_prefix:
            module = '%s/%s' % (self.module_prefix, module)
        module = '__'.join([i for i in module.split('/') if i])
        method = getattr(self, module or 'index', None)
        if method and module not in ('get', 'post'):
            try:
                result = method()
                if result:
                    self.send_json(result)
            except Exception as ex:
                logging.error('%s\n%s\n', self.request, str(ex), exc_info=True)
                self.send_json(None, E_INTER, str(ex))
        else:
            raise tornado.web.HTTPError(404)

    def get(self, module):
        '''
        HTTP GET处理
        '''
        self.process_module(module)

    def post(self, module):
        '''
        HTTP POST处理
        '''
        self.process_module(module)


class BaseInnerAPIHandler(BaseHandler):
    ''' 内部API Handler
    '''

    def get_argument(
            self, name, default=tornado.web.RequestHandler._ARG_DEFAULT,
            strip=True):
        '''重写以把unicode的参数都进行utf-8编码
        '''
        value = super(BaseInnerAPIHandler, self).get_argument(name, default, strip)
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        return value

    def render_json(self, jsonable):
        ''' 渲染json
        '''
        self.set_header("Content-Type", "application/json")
        jsonable = force_utf8_new(jsonable)
        self.finish(json.dumps(jsonable, default=json_default))

    def send_json(self, body, code, msg=""):
        ''' 渲染json
        '''
        self.render_json({'code': code, 'msg': msg, 'body': body})

    def _get(self):
        raise HTTPError(405)

    def _post(self):
        raise HTTPError(405)

    @exception_control
    def get(self):
        return self._get()

    @exception_control
    def post(self):
        return self._post()


class CoroutingHandler(BaseHandler):
    """
    异步handler
    """

    @tornado.gen.coroutine
    def _get(self):
        raise HTTPError(405)

    @tornado.gen.coroutine
    def _post(self):
        raise HTTPError(405)

    @tornado.gen.coroutine
    def get(self):
        result = yield self._get()
        if result:
            self.send_json(result)

    @tornado.gen.coroutine
    def post(self):
        result = yield self._post()
        if result:
            self.send_json(result)

    @tornado.gen.coroutine
    def send_json_2(self, res, code=E_SUCC, msg=None):
        '''发送json数据, 要逐步替代send_json
        {
            'code':'状态码',
            'msg':'错误信息',
            'body':'数据内容'
        }
        '''
        result = {'code': code, 'msg': msg, 'body': res}
        result = json.dumps(result, default=json_default)
        self.finish(result)

    @tornado.gen.coroutine
    def sleep(self, sleep_time):
        """
        睡眠时间
        :param sleep_time:
        :return:
        """
        yield tornado.gen.sleep(sleep_time)

def route(pattern):
    ''' 自动路由装饰器
    '''

    def decorator(cls):
        ''' 类装饰器
        '''
        assert issubclass(cls, BaseHandler), "route只用来装饰handler"
        auto_route_handlers.append((pattern, cls))
        return cls

    return decorator


def json_default(obj):
    '''实现json包对datetime的处理
    '''
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, datetime.date):
        raise TypeError('%r is not JSON serializable' % obj)

if __name__ == '__main__':
    baseHandler = BaseHandler()
    print 123