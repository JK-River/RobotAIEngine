#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：景观语义
  创 建 者：余菲
  创建日期：16/6/16
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, directional, sight_name, any_w
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty, attach_name

class Sight(object):
    # 标识是sight领域
    service = 'sight'

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
    directional = directional.join_all
    sight_name = sight_name.join_all

    prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
    postfix = o(auxiliary, prep, pronoun)
    infix = o(prep, pronoun, degree)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)
    infix_0_2 = r(infix, 0, 2)

    sight_name = attach_name(sight_name, 'name')

    sight = r('(把|将)', 0, 1) + sight_name

    shape = '(样子|形状|外表|图片)'
    what = '(什么|哪种|怎么)'
    look = '(看看|观看|查看|看|瞧|瞅|瞄|观赏|欣赏)' + e(numeral) + e(quantifier)

    show = '(显示|出现|演示|表演)' + e(directional) + e(numeral) + e(quantifier)

    # 查询表达方式1：雪山
    sight_case1 = sight
    rule_sight_case1 = Rule(attach_perperty(sight_case1, {'operation': 'query', 'rule': 1}))

    # 查询表达方式2：我想看一下雪山
    sight_case2 = prefix_0_5 + look + e(infix) + sight + postfix_0_3
    rule_sight_case2 = Rule(attach_perperty(sight_case2, {'operation': 'query', 'rule': 2}))

    # 查询表达方式3：你把雪山显示给我看看；雪山显示出来给我看看；雪山显示一下看看；
    sight_case3 = prefix_0_5 + sight + e(show) + infix_0_2 + look + postfix_0_3
    rule_sight_case3 = Rule(attach_perperty(sight_case3, {'operation': 'query', 'rule': 3}))

    # 查询表达方式4：显示雪山；显示出来雪山看看；
    sight_case4 = prefix_0_5 + show + e(infix) + sight + e(look) + postfix_0_3
    rule_sight_case4 = Rule(attach_perperty(sight_case4, {'operation': 'query', 'rule': 4}))

    # 查询表达方式5：雪山是什么样子的
    sight_case5 = prefix_0_5 + sight + '(是)?' + what + shape + postfix_0_3
    rule_sight_case5 = Rule(attach_perperty(sight_case5, {'operation': 'query', 'rule': 5}))
