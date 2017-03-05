#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：智能家居基类
  创 建 者：余菲
  创建日期：17/2/14
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual, any_w, stop_words

from utils.utils import o, r, e, attach_perperty, range_tag

pronoun = pronoun.join_all
modals = modals.join_all
prep = prep.join_all
degree = degree.join_all
honorific = honorific.join_all
interj = interj.join_all
prefix_unsual = prefix_unsual.join_all
auxiliary = auxiliary.join_all
quantifier = quantifier.join_all
numeral = numeral.join_all
adjective = adjective.join_all
adverb = adverb.join_all
stop_words = stop_words.join_all
want = '(要|想要|想|需要)'

prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
postfix = o(auxiliary, prep, pronoun)
infix = o(prep, pronoun, degree)

prefix_0_5 = r(prefix, 0, 5)
prefix_0_3 = r(prefix, 0, 3)
postfix_0_3 = r(postfix, 0, 3)

# 位置
bedroom = attach_perperty('(卧室|卧房|睡房)', {'position': 'bedroom'})
main_bedroom = attach_perperty('(主卧)', {'position': 'main_bedroom'})
second_bedroom = attach_perperty('(次卧)', {'position': 'second_bedroom'})
living_room = attach_perperty('(客厅)', {'position': 'living_room'})
kitchen = attach_perperty('(厨房)', {'position': 'kitchen'})
dining_room = attach_perperty('(餐厅)', {'position': 'dining_room'})
bath_room = attach_perperty('(卫生间)', {'position': 'bath_room'})
position = o(bedroom, main_bedroom, second_bedroom, living_room, kitchen, dining_room, bath_room) + e('的')

# 动作特征词
turn_on = attach_perperty('开|打开', {'operation': 'turn_on'})
turn_off = attach_perperty('(关上|关闭|关下|关一下|关掉|关)', {'operation': 'turn_off'})
turn_up = attach_perperty('(调高|升高|升起来)', {'operation': 'turn_up'})
turn_down = attach_perperty('(调低|降低|降下来)', {'operation': 'turn_down'})

desc = range_tag(6, 'desc')