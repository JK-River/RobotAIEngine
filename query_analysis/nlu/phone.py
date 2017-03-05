#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：电话语义
  创 建 者：余菲
  创建日期：16/12/17
"""
from dict.dict import pronoun, adverb, modals, stop_words, honorific, any_w
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag


class Phone(object):
    # 标识是phone领域
    service = 'phone'

    pronoun = pronoun.join_all
    can_words = modals.join_all
    adverb = adverb.join_all
    ask = honorific.join_all
    want = '(要|想要|想|需要)'

    # 语义意图，仅支持一种，打
    dial = '(打|挂｜拨)(一)?(个)?'

    # 电话
    phone = '(电话)'

    # robot
    robot = '(你|机器人|小忆)'

    # me
    me = '(我|我们|咱|咱们|俺)'

    # 再，又
    again = '(再|又|多)'

    # 关系
    relation = '(爸爸|妈妈|爷爷|奶奶)'
    relation = attach_name(relation, 'relation')

    # 个
    an = '(个|一个)'

    # 给
    give = '(给)'

    # 我要打电话
    case_1 = e(robot) + e(me) + e(want) + e(again) + dial + e(an) + phone + e(stop_words)
    rule_1 = Rule(attach_perperty(case_1, {'scene': 'phone_call', 'operation': 'phone', 'rule': 1}))

    # 给爸爸打电话
    case_2 = give + relation + dial + phone
    rule_2 = Rule(attach_perperty(case_2, {'operation': 'phone', 'rule': 2}))
