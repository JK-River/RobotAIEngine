#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：演示简单使用方法
  创 建 者：余菲
  创建日期：17/3/5
"""
# test_rule.py
from nlu.nlu_framework import Nlu_Framework
from nlu.rule import Rule
from utils.utils import range_tag, attach_perperty


class Test(object):
    # 标识是test领域(这个service字段必须存在，命中本类中正则时，会输出这个字段)
    service = 'test'
    # 表示抓取2个字长度的信息,输出字段为name
    name = range_tag(2, 'user_name')

    # 正则规则：我的名字是小明
    name_case1 = '我的名字是' + name

    # 生成规则对象
    rule_case1 = Rule(attach_perperty(name_case1, {'operation': 'query', 'rule': 1}))

Nlu_Framework.register(Test)

match_dict_list = Nlu_Framework.match('我的名字是小明')

for k, v in match_dict_list[0].items():
    print '{} : {}'.format(k, v)
