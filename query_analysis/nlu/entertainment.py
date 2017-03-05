#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：游戏语义
  创 建 者：余菲
  创建日期：16/6/19
"""

from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, stop_words
from nlu.rule import Rule

from utils.utils import o, r, e, range_tag, attach_perperty, attach_name


class Entertainment(object):
    # 标识是entertainment领域
    service = 'entertainment'

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

    prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
    postfix = o(auxiliary, prep, pronoun)
    infix = o(prep, pronoun, degree)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    play = '(玩|玩儿|打开|启动)'
    game = '(的)?' + '(游戏|程序|软件)'
    name = range_tag(12, 'name')

    names_1 = '认知'
    names_1 = attach_perperty(names_1, {'id':1})
    names_2 = '英语'
    names_2 = attach_perperty(names_2, {'id':2})
    names = o(names_1, names_2)
    names = attach_name(names, 'name')

    study = '(学习)'

    # 游戏语义解析
    game_case1 = prefix_0_5 + play + e(name) + e(study) + game + postfix_0_3    # 玩 [xxx] 游戏
    rule_game_case1 = Rule(attach_perperty(r(game_case1, 1, 3), {'operation': 'start', 'rule': 1}))
    game_case2 = prefix_0_5 + play + names + e(study) + game + postfix_0_3  # 玩 认知 游戏
    rule_game_case2 = Rule(attach_perperty(r(game_case2, 1, 3), {'operation': 'start', 'rule': 2}))
    game_case3 = names + game   # 认知 游戏
    rule_game_case3 = Rule(attach_perperty(r(game_case3, 1, 3), {'operation': 'start', 'rule': 3}))
    game_case4 = names + study  # 英语 学习
    rule_game_case4 = Rule(attach_perperty(r(game_case4, 1, 3), {'operation': 'start', 'rule': 4}))
