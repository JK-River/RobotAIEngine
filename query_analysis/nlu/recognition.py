#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：物体语义
  创 建 者：余菲
  创建日期：16/6/19
"""

from dict.dict import pronoun, modals, adverb, stop_words, any_w
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag


class Recognition(object):
    # 标识recognition领域
    service = 'recognition'

    stop_words = stop_words.join_all
    pronoun = pronoun.join_all
    modals = modals.join_all
    adverb = adverb.join_all

    look = '(看|猜|说|查看|瞅|瞧|观察|鉴别|望|瞟|问|告诉我)'
    location = '(这|那|这边|那边|这里|那里|这个)'
    what = '(什么|啥)'
    robot = '(你|机器人|小忆)'

    color = '(颜色|彩色|色|色泽|红|黄|蓝|绿|黑|白|紫|桔|橙|青)'
    color = attach_perperty(color, {'attribute': 'color'})

    thing = '(东西|物品|水果)'
    thing = attach_perperty(thing, {'attribute': 'name'})

    # 这是什么颜色
    color_case = '(请|那)?' + e(robot) + e(look) + e(location) + '是' + what + color + any_w
    rule_color_case = Rule(attach_perperty(color_case, {'operation': 'get', 'attribute': 'color'}))

    # 这是什么
    thing_case = '(请|那)?' + e(robot) + e(look) + location + '是' + what + e(thing) + any_w
    rule_thing_case = Rule(attach_perperty(thing_case, {'operation': 'get', 'attribute': 'name'}))
