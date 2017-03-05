#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：灯光控制
  创 建 者：余菲
  创建日期：17/2/11
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual, any_w, stop_words
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty, range_tag

from smart_home_common import *

class Light(object):

    # 标识是Light领域
    service = 'smart_home_light'

    # 动作特征词
    turn = o(turn_on, turn_off)
    light = e(desc) + e('的') + o('灯', '灯光')

    # [灯]控制语义解析
    light_case1 = prefix_0_3 + turn + e(position) + light + postfix_0_3    # 关灯
    rule_comic_case_1 = Rule(attach_perperty(light_case1, {'rule': 1}))

    light_case2 = prefix_0_3 + e('把') + e('position') + light + turn + postfix_0_3     # 把灯打开
    rule_comic_case_2 = Rule(attach_perperty(light_case2, {'rule': 2}))
