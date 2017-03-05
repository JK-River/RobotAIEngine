#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：空气净化器
  创 建 者：余菲
  创建日期：17/2/14
"""
from nlu.rule import Rule

from smart_home_common import *

class Aircleaner(object):
    # 标识是smart_home_aircleaner领域
    service = 'smart_home_aircleaner'

    # 动作特征词
    turn = o(turn_on, turn_off)
    query = attach_perperty(o('查一下', '查询', '查查', '怎么样'), {'operation': 'query'})
    aircleaner = e(desc) + e('的') + o('空气净化器', '空净') + e('的')
    airquality = e(aircleaner) + o('空气质量', '空气');

    volume = attach_perperty('音量', {'parameter': 'volume'})
    channel = attach_perperty('频道', {'parameter': 'channel'})
    rack = attach_perperty('架', {'parameter': 'rack'})
    parameter = o(volume, channel, rack)

    # [空净]控制语义解析
    aircleaner_case1 = prefix_0_3 + turn + e(position) + aircleaner + e(parameter) + postfix_0_3    # 关空气净化器
    rule_aircleaner_case1 = Rule(attach_perperty(aircleaner_case1, {'rule': 1}))

    aircleaner_case2 = prefix_0_3 + e('把') + e('position') + aircleaner + e(parameter) + turn + postfix_0_3     # 把空气净化器打开
    rule_aircleaner_case2 = Rule(attach_perperty(aircleaner_case2, {'rule': 2}))

    aircleaner_case3 = prefix_0_3 + e('把') + e('position') + aircleaner + query + postfix_0_3   # 卧室的空气质量查一下
    rule_aircleaner_case3 = Rule(attach_perperty(aircleaner_case3, {'rule': 2}))

    aircleaner_case4 = prefix_0_5 + e('把') + query + e('position') + aircleaner + postfix_0_3   # 卧室的空气质量查一下
    rule_aircleaner_case4 = Rule(attach_perperty(aircleaner_case4, {'rule': 2}))
