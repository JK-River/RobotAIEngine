#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：窗帘控制
  创 建 者：余菲
  创建日期：17/2/11
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual, any_w, stop_words
from nlu.rule import Rule

from smart_home_common import *

class Curtain(object):
    # 标识是mode领域
    service = 'smart_home_curtain'

    # 动作特征词
    turn = o(turn_on, turn_off, turn_up, turn_down)
    tv = e(desc) + e('的') + o('电视机', '电视') + e('的')

    volume = attach_perperty('音量', {'parameter': 'volume'})
    channel = attach_perperty('频道', {'parameter': 'channel'})
    rack = attach_perperty('架', {'parameter': 'rack'})
    parameter = o(volume, channel, rack)

    # [电视]控制语义解析
    tv_case1 = prefix_0_3 + turn + e(position) + tv + e(parameter) + postfix_0_3    # 关灯
    rule_tv_case_1 = Rule(attach_perperty(tv_case1, {'rule': 1}))

    tv_case2 = prefix_0_3 + e('把') + e(position) + tv + e(parameter) + turn + postfix_0_3     # 把灯打开
    rule_tv_case_2 = Rule(attach_perperty(tv_case2, {'rule': 2}))
