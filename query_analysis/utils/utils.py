#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：
  创 建 者：余菲
  创建日期：16/6/4
"""
from collections import defaultdict


def attach_name(case, name):
    """
    对某个case附加一个名字属性(这种属性只有1个对象如type或name等)
    :param case: case的string 如(虫|鸟)
    :param name: type或name
    :return:
    """
    return "(?P<{}>({}))".format(name, case)


def attach_perperty(case, perperty):
    """
    对某个case附加一个或一组属性(这种属性是有2个对象的如 {'operation':'query'})
    (对于必须出现重复的attach_string,可以采用在最后加三下划线的方法规避, 如:'operation':'query___')
    注意只能在最后加才可以正确捕获
    :param case: case的string表示如:(我|咱)(想|要)看(老虎|狮子)
    :param perperty: {'operation':'query'}
    :return:
    """
    perperty_string = '__'.join(['{}__{}'.format(k, v) for k, v in perperty.items()])
    return "(?P<{}>({}))".format(perperty_string, case)


def get_attach_perperty(attach_string):
    """
    取得附加的属性值(对于必须出现重复的attach_string,可以采用在最后加双下划线的方法规避)
    :param attach_string: 附加属性的字符串 'operation_query'
    :return: {'a':'b'} --附加属性的dict
    """
    if not attach_string or len(attach_string.strip()) == 0:
        return {}
    attach_array = attach_string.split('__')
    assert len(attach_array) % 2 == 0, 'attach_string is error: %s' % attach_string
    attach_perperty = defaultdict(dict)
    for k in range(len(attach_array) / 2):
        if attach_array[k*2] and attach_array[k*2+1]:
            attach_perperty[attach_array[k*2]] = attach_array[k*2+1]
    return attach_perperty


def e(expression):
    """
    either 可选, 表明这个experssion是可出现,可不出现的
    :param expression:
    :return: (expression)?
    """
    return '({})?'.format(expression)


def o(*args):
    """
    OR 表明这2个expression是可选的
    :param experssion1:
    :param expression2:
    :return:
    """
    template = '|'.join(args)
    return "({})".format(template)


def r(expression, min, max):
    """
    repeat 表明这个expression可重复的次数
    :param expression:
    :param min: 最小重复次数
    :param max: 最大重复次数
    :return:
    """
    return "((%s){%s,%s})" % (expression, min, max)


def range_tag(length, name=None, start=1):
    """
    返回一个范围字段
    :param name:
    :param length:
    :param start:最小的出现次数
    :return:
    """
    if name:
        return '(?P<%s>(.){%s,%s})' % (name, start, length*3)
    return '((.){%s,%s})' % (start, length*3)


def range_not_tag(length, tag, name=None, start=1):
    """
    返回一个范围字段，此时抓取的信息不能是tag字段
    :param length:
    :param tag:
    :param name:
    :param start:
    :return:
    """
    if name:
        return '(?P<%s>(((?!%s).)*){%s,%s})' % (name, tag, start, length*3)


def force_utf8(data, force_key=False):
    '''
    数据转换为utf8
    @data: 待转换的数据
    @return: utf8编码
    '''
    if force_key:
        return force_utf8_new(data)
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, list):
        for idx, i in enumerate(data):
            data[idx] = force_utf8(i)
    elif isinstance(data, dict):
        for i in data:
            data[i] = force_utf8(data[i])
    return data

def force_utf8_new(data):
    '''
    数据转换为utf8，如果是字典key 也需要转化
    数据转换为utf8
    @data: 待转换的数据
    @return: utf8编码
    '''
    if isinstance(data, dict):
        return {force_utf8_new(key): force_utf8_new(value) for key, value in data.iteritems()}
    elif isinstance(data, list):
        return [force_utf8_new(element) for element in data]
    elif isinstance(data, tuple):
        return [force_utf8_new(element) for element in data]
    elif isinstance(data, unicode):
        return data.encode('utf-8')
    else:
        return data