#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：屏幕显示
  创 建 者：余菲
  创建日期：16/6/10
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty


class Display(object):
    # 标识是display领域
    service = 'display'

    pronoun = pronoun.join_all
    modals = modals.join_all
    prep = prep.join_all
    degree = degree.join_all
    honorific = honorific.join_all
    interj = interj.join_all
    prefix_unsual = '(今天|现在)'
    auxiliary = auxiliary.join_all
    quantifier = quantifier.join_all
    numeral = numeral.join_all
    adjective = adjective.join_all
    adverb = adverb.join_all

    prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
    postfix = o(auxiliary, prep, pronoun)
    infix = o(prep, pronoun, degree)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    # 调整特征词
    change_up = "(增|加|升|扩)" + e(numeral) + e(quantifier)
    change_up = attach_perperty(change_up, {'direction': 'up'})
    change_down = "(减|降|缩)" + e(numeral) + e(quantifier)
    change_down = attach_perperty(change_down, {'direction': 'down'})
    change = "(调|调整|弄|搞|放|变|整)"

    # 方向-向上
    up = "(亮|大|高|强|重)" + e(numeral) + e(quantifier)
    up = attach_perperty(up, {'direction': 'up'})
    light_up = "(亮|白)" + e(numeral) + e(quantifier)
    light_up = attach_perperty(light_up, {'direction': 'up'})
    size_up = "(大|高|宽|胖)" + e(numeral) + e(quantifier)
    size_up = attach_perperty(size_up, {'direction': 'up'})

    # 方向-向下
    down = "(暗|小|低|弱|轻|低沉)" + e(numeral) + e(quantifier)
    down = attach_perperty(down, {'direction': 'down'})
    light_down = "(暗|黑)" + e(numeral) + e(quantifier)
    light_down = attach_perperty(light_down, {'direction': 'down'})
    size_down = "(小|矮|窄|瘦)" + e(numeral) + e(quantifier)
    size_down = attach_perperty(size_down, {'direction': 'down'})

    # 方向-最大
    maximum = e("(到|至)") + "(最大|最高|最强|最重|最响|最亮)"
    maximum = attach_perperty(maximum, {'direction': 'up', 'step': 'toend'})
    light_maximum = e("(到|至)") + "(最亮)"
    light_maximum = attach_perperty(light_maximum, {'direction': 'up', 'step': 'toend'})
    size_maximum = e("(到|至)")+ "(最大)"
    size_maximum = attach_perperty(size_maximum, {'direction': 'up', 'step': 'toend'})

    # 方向-最小
    minimum = e("(到|至)") + "(最小|最低|最弱|最轻)"
    minimum = attach_perperty(minimum, {'direction': 'down', 'step': 'toend'})
    light_minimum = e("(到|至)") + "(最暗)"
    light_minimum = attach_perperty(light_minimum, {'direction': 'down', 'step': 'toend'})
    size_minimum = e("(到|至)") + "(最小)"
    size_minimum = attach_perperty(size_minimum, {'direction': 'down', 'step': 'toend'})

    # 方向-汇总
    direction = o(up, down, maximum, minimum) # 强一点
    light_direction = o(light_up, light_down, light_maximum, light_minimum) # 亮一点
    size_direction = o(size_up, size_down, size_maximum, size_minimum) # 大一点

    # 调整+方向
    change_case1 = o(change_up, change_down) + e(degree) + e(direction) # 加[重]
    change_case2 = e(change) + e(degree) + e(degree) + direction # [调]大
    change_case3 = "(往|向|朝)" + e(degree) + e(degree) + direction + e(change) # 往大[调]
    change_direction = o(change_case1, change_case2, change_case3)

    # 调整+亮度方向
    change_light_case1 = e(o(change, change_up, change_down)) + e(degree) + e(degree) + light_direction # [调]暗
    change_light_case2 = "(往|向|朝)" + e(degree) + e(degree) + light_direction + e(o(change, change_up, change_down)) # 往暗[调]
    change_light_direction = o(change_light_case1, change_light_case2)

    # 调整+大小方向
    change_size_case1 = e(o(change, change_up, change_down)) + e(degree) + e(degree) + size_direction # [调]大
    change_size_case2 = "(往|向|朝)" + e(degree) + e(degree) + size_direction + e(o(change, change_up, change_down)) # 往暗[调]
    change_size_direction = o(change_size_case1, change_size_case2)

    # 屏幕调节特征词
    display = "(把|将)?" + "(显示|屏|屏幕|图像|图片|界面)" + e(numeral) + e(quantifier)
    light = "(把|将)?" + "(亮度)" + e(numeral) + e(quantifier)
    size = "(把|将)?" + "(大小|尺寸)" + e(numeral) + e(quantifier)

    # 亮度表达方式
    display_light1 = prefix_0_5 + r(display,0, 2) + light + e(infix) + change_direction + postfix_0_3 # [把屏幕] 亮度 调高
    display_light2 = prefix_0_5 + r(display,0, 2) + e(infix) + change_direction + light + postfix_0_3 # [把屏幕] 调高 亮度
    display_light3 = prefix_0_5 + r(display,0, 2) + e(infix) + change_light_direction + postfix_0_3 # [屏幕] 调亮
    display_light4 = prefix_0_5 + change_direction + r(display, 0, 2) + light + postfix_0_3 # //调高 [屏幕] 亮度
    display_light_sentence = o(display_light1, display_light2, display_light3, display_light4)
    display_light_sentence = attach_perperty(display_light_sentence, {'operation': 'light', 'rule': 1})
    rule_display_light_sentence = Rule(r(display_light_sentence, 1, 3))

    # 大小表达方式：屏幕再调大点；请你把屏幕调到最小可以吗；把屏幕调整更大一点；
    display_size1 = prefix_0_5 + r(display, 0, 2) + size + e(infix) + change_direction + postfix_0_3 # [把屏幕] 大小 调高
    display_size2 = prefix_0_5 + r(display, 0, 2) + e(infix) + change_direction + size + postfix_0_3 # [把屏幕] 调高 大小
    display_size3 = prefix_0_5 + r(display, 0, 2) + e(infix) + change_size_direction + postfix_0_3 # [屏幕] 调大
    display_size4 = prefix_0_5 + change_direction + r(display, 0, 2) + size + postfix_0_3 # 调高 [屏幕] 亮度
    display_size_sentence = o(display_size1, display_size2, display_size3, display_size4)
    display_size_sentence = attach_perperty(display_size_sentence, {'operation': 'size', 'rule': 2})
    rule_display_size_sentence = Rule(r(display_size_sentence, 1, 3))
