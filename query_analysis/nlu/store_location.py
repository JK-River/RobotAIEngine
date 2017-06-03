#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,掌阅科技
  All rights reserved.

  摘    要：储物位置（小忆我告诉你xx放在xx/小忆我问你xx放在哪里）
  创 建 者：余菲
  创建日期：17/5/6
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, stop_words, vehicle_name
from nlu.rule import Rule

from utils.utils import o, r, e, range_tag, attach_perperty, range_not_tag


class StoreLocation(object):
    # 标识是store_location领域
    service = 'store_location'

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

    # 如果结尾使用非则会导致完全不匹配而失败
    set_location_1_5 = range_tag(5, name='location', start=1)

    # 为了解决相近的（放|在|放在）问题使用非贪婪
    object_1_5 = '(?P<object>(.)+?)'
    location_1_5 = '(?P<location>(.)+?)'

    set_prefix = '(小忆我告诉你)'
    query_prefix = '(小忆我问你)'

    put = '(放在|在)'

    keep = '((在)|(放)|(放在))'

    where = o('哪里', '什么地方', '什么位置')

    # 设置位置表达方式1：
    set_case1 = set_prefix + object_1_5 + put + set_location_1_5
    rule_set_case1 = Rule(attach_perperty(set_case1, {'operation': 'set', 'rule': 1}))

    # 查询位置表达方式1：
    query_case1 = query_prefix + object_1_5 + keep + where + e(stop_words)
    rule_query_case1 = Rule(attach_perperty(query_case1, {'operation': 'query', 'rule': 2}))

