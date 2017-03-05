#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：电量语义
  创 建 者：余菲
  创建日期：16/6/19
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty

class Battery(object):
    # 标识是battery领域
    service = 'battery'

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

    prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
    postfix = o(auxiliary, prep, pronoun)
    infix = o(prep, pronoun, degree)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    query = '(查|查询|告诉我)(下)?'
    howmuch = '(多少|百分之多少|百分之几|几个|几格)'
    left = '(还)?(剩|剩余|剩下|有)' + e(howmuch)
    power = '(的)?(电量|电|电池)'

    # [剩余电量]语义解析：电量/查电量/告诉我电量/还剩多少电量/电量剩多少
    battery_case1 = prefix_0_5 + e(query) + left + power + postfix_0_3  # [查询] 剩余 电量
    battery_case2 = prefix_0_5 + e(query) + power + left + postfix_0_3  # [查询] 电量 剩余
    battery_case3 = e(query) + power    # 电量

    battery_sentence = o(battery_case1, battery_case2, battery_case3)
    rule_battery_sentence = Rule(attach_perperty(r(battery_sentence, 1, 3), {'operation': 'get', 'rule': 1}))
