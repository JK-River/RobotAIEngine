#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：Rule规则的实现类
  创 建 者：余菲
  创建日期：16/12/31
"""
from collections import Counter

import regex as re


class Rule(object):
    """
    对于规则的封装类
    """

    duplicate_key_re = re.compile(r"<([^>]*)>")

    def __init__(self, rule_str, filter_list={}):
        """
        初始化
        :param rule_str: 规则文本
        :param filter_list: 支持的filter列表['filter1', 'filter2']
        """
        self.rule_str = rule_str
        self.filters = filter_list
        self.rule = re.compile(self._fix_duplicate(rule_str), max_mem=1024 * 1024 * 100)

    def is_match(self, filter_name):
        """
        是否match指定filter,对本filter_list
        :param filter_name: 过滤器名
        :return:
        """
        return filter_name in self.filters

    def match(self, query_string):
        """
        看本规则是否匹配query_string
        :param query_string: 文本信息
        :return:
        """
        return self.rule.match(query_string)

    def _fix_duplicate(self, re_string):
        """
        对需要获取的部分进行去重复(在其后加___),正则表达式不支持在同一句中出现重复的捕获字段,
        所以对于出现相同的捕获字段,需要去重复(通过加___处理)
        :param re_string:
        :return:
        """
        duplicate_key_list = self.duplicate_key_re.findall(re_string)

        # 判断是否有重复key
        if len(set(duplicate_key_list)) == len(duplicate_key_list):
            return re_string

        for key, value in Counter(duplicate_key_list).items():
            if value > 1:
                for k in range(value):
                    # 注意这里替换的时候,必须要带上<>,否则会把有包含关系的东西替换掉如:direction_up与direction_up_step_toend
                    re_string = re_string.replace("<{}>".format(key), "<{}>".format(key + (k + 1) * '___'), 1)

        # 是否替换成了相同的key, 使用递归解决此问题
        re_string = self._fix_duplicate(re_string)
        return re_string
