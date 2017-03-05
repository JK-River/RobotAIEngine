#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：交通工具
  创 建 者：余菲
  创建日期：16/6/11
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, stop_words, vehicle_name
from nlu.rule import Rule

from utils.utils import o, r, e, range_tag, attach_perperty


class Vehicle(object):
    # 标识是vehicle领域
    service = 'vehicle'

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
    stop_words = stop_words.join_all
    vehicle = vehicle_name.join_all

    ti_ch_0_3 = range_tag(3, start=0)

    show = '(样子|形状|外表|图片)'
    what = '(什么|哪种|怎么|啥)'
    append = '(加|增加|添加|加上|补充|再|再来|再加|再次|再一次|继续|接着)'
    append = attach_perperty(append, {'operation': 'append'})

    # me
    me = '(我|我们|咱|咱们|俺)'

    # ask
    ask = '(请|让|要|要求|麻烦)'

    # 再，又
    again = '(再|又|多)'

    # robot
    robot = '(你|机器人|小忆)'

    want = '(要|想|想要|需要|能)'

    look = '(放|来|看|给)' + e('一') + e('个|辆')
    look = attach_perperty(look, {'operation': 'name'})

    # 消防车是什么样子的
    case1 = ti_ch_0_3 + vehicle + ti_ch_0_3 + what + show + e(stop_words)
    rule_case1 = Rule(attach_perperty(case1, {'operation': 'name', 'rule': 1}))

    # 我能请你给我看下自行车
    case2 = e(me) + e(want) + e(again) + e('请') + e(robot) + e(look) + e(me) + e(adverb) + look + e('下') + vehicle + e(stop_words)
    rule_case2 = Rule(attach_perperty(case2, {'operation': 'query', 'rule': 2}))

    # 小忆我要自行车
    case3 = e(robot) + me + e(want) + e(look) + vehicle + e(stop_words)
    rule_case3 = Rule(attach_perperty(case3, {'operation': 'query', 'rule': 3}))

    # 消防车是干什么的
    case4 = ti_ch_0_3 + vehicle + '(是)' + ti_ch_0_3 + what + ti_ch_0_3 + '(用)?' + ti_ch_0_3
    rule_case4 = Rule(attach_perperty(case4, {'operation': 'query', 'rule': 4}))

    # 自行车
    case5 = vehicle + e('我要看') + e(stop_words)
    rule_case5 = Rule(attach_perperty(case5, {'operation': 'query', 'rule': 5}))

    # 小忆你有没有自行车
    case6 = e(robot) + e('你') + '(有没有)' + vehicle + e('我') + e('要') + e('看') + e(stop_words)
    rule_case6 = Rule(attach_perperty(case6, {'operation': 'query', 'rule': 6}))

    # 再加一辆自行车
    case7 = ti_ch_0_3 + append + ti_ch_0_3 + quantifier + vehicle + ti_ch_0_3
    rule_case7 = Rule(attach_perperty(case7, {'operation': 'append', 'rule': 7}))
