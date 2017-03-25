#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：脑筋急转弯语义
  创 建 者：余菲
  创建日期：16/12/17
"""
from dict.dict import pronoun, adverb, modals, stop_words, honorific, any_w
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag


class Trick(object):
    # 标识是trick领域
    service = 'trick'

    pronoun = pronoun.join_all
    can_words = modals.join_all
    adverb = adverb.join_all
    ask = honorific.join_all
    want = '(要|想|想要|需要)'

    # 语义意图，仅支持一种，听
    listen = '(听)(一)?(个)?'

    # 语义意图
    tell = '(讲|来)(一)?(个)?'

    # 脑筋急转弯
    trick = '(脑筋急转弯|急转弯)'

    # robot
    robot = '(你|机器人|小忆)'

    # me
    me = '(我|我们|咱|咱们|俺)'

    # 再，又
    again = '(再|又|多)'

    # 个
    an = '(个|一个)'

    # 给
    give = '(给|为)'

    # 我要听个急转弯
    case_1 = e(robot) + e(me) + e(want) + e(again) + listen + e(an) + trick + e(stop_words)
    rule_1 = Rule(attach_perperty(case_1, {'scene': 'trick', 'operation': 'trick', 'rule': 1}))

    # 给我讲个急转弯
    case_2 = e(robot) + e(give) + e(me) + tell + e(an) + trick + e(stop_words)
    rule_2 = Rule(attach_perperty(case_2, {'scene': 'trick', 'operation': 'trick', 'rule': 2}))

    # 再来一个
    case_3 = attach_perperty('(再来一个)', {'scene': 'trick', 'operation': 'trick', 'rule': 3})
    rule_3 = Rule(case_3, {'status': 'trick'})
