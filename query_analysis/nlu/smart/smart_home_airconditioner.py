#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：空调
  创 建 者：余菲
  创建日期：17/2/14
"""

from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual, any_w, stop_words
from nlu.rule import Rule

from smart_home_common import *

class Curtain(object):
    # 标识是mode领域
    service = 'smart_home_airconditioner'

    # 动作特征词
    turn = o(turn_on, turn_off, turn_up, turn_down)
    airconditioner = e(desc) + e('的') + o('空调机', '空调') + e('的')

    temperature = '(温度)'
    cool = attach_perperty('(制冷|冷风)', {'parameter': 'cool'})
    heat = attach_perperty('(制热|热风)', {'parameter': 'heat'})
    parameter = o(temperature, cool, heat) + e('调到')
    parameter = attach_perperty(parameter, {'operation': 'set'})

    degree = range_tag(2, 'degree') + '(度)'

    # [空调]控制语义解析
    airconditioner_case1 = prefix_0_3 + turn + e(position) + airconditioner + e(parameter) + postfix_0_3    # 关空调
    rule_conditioner_case_1 = Rule(attach_perperty(airconditioner_case1, {'rule': 1}))

    airconditioner_case2 = prefix_0_3 + e('把') + e(position) + airconditioner + e(parameter) + turn + postfix_0_3     # 把空调打开
    rule_conditioner_case_2 = Rule(attach_perperty(airconditioner_case2, {'rule': 2}))

    airconditioner_case3 = prefix_0_5 + '(把)' + e(position) + airconditioner + parameter + e(turn) + degree + postfix_0_3   # 空调冷风16度
    rule_conditioner_case_3 = Rule(attach_perperty(airconditioner_case3, {'rule': 3}))
