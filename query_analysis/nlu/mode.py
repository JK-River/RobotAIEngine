#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：运行模式
  创 建 者：余菲
  创建日期：16/6/11
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty

class Mode(object):
    # 标识是mode领域
    service = 'mode'

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

    prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
    postfix = o(auxiliary, prep, pronoun)
    infix = o(prep, pronoun, degree)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    # 动作
    action_enter = "(进入|进|启动|开启)" + e(numeral) + e(quantifier)
    action_enter = attach_perperty(action_enter, {'operation': 'enter'})
    action_quit = "(退出|退)" + e(numeral) + e(quantifier)
    action_quit = attach_perperty(action_quit, {'operation': 'quit'})
    action = o(action_enter, action_quit)

    # 模式
    mode_show = "(展会|展览|参展|展厅|展示)"
    mode_show = attach_perperty(mode_show, {'name': 'show'})
    mode_dance = "(跳舞|舞蹈)"
    mode_dance = attach_perperty(mode_dance, {'name': 'dance'})
    mode_emotion = "(表情|舞蹈)"
    mode_emotion = attach_perperty(mode_emotion, {'name': 'emotion'})
    mode_attract = "(招揽|招来|招徕|揽客)"
    mode_attract = attach_perperty(mode_attract, {'name': 'attract'})
    mode_term = '(运行|运新|运型)?' + '(模式|方式|形式|样式|招式|状态|情景|表演)'
    action_mode = '(把|将)?' + o(mode_show, mode_dance, mode_emotion, mode_attract) + mode_term

    # 查询
    query = '(查询|查|显示)' + e(numeral) + e(quantifier)
    current = '(当前|现在|目前|眼下)' + e('的')
    what = e('是') + '(什么|哪个|多少|怎样|如何|什么样)'

    # 进入退出表达方式
    action_case1 = prefix_0_5 + action + action_mode + postfix_0_3  # 启动 展会模式
    action_case2 = prefix_0_5 + action_mode + action + postfix_0_3  # 展会模式 开启
    action_case3 = prefix_0_5 + mode_term + action_quit + postfix_0_3  # 运行模式 退出
    action_sentence = o(action_case1, action_case2, action_case3)
    rule_action_sentence = Rule(attach_perperty(action_sentence, {'rule': '1'}))

    # 查询表达方式
    get_case1 = prefix_0_5 + query + e(current) + mode_term + postfix_0_3  # 显示 [当前] 模式
    get_case2 = prefix_0_5 + current + what + mode_term + postfix_0_3  # 现在是哪个运行模式
    get_case3 = prefix_0_5 + current + mode_term + what + postfix_0_3  # 现在的运行模式是哪个
    get_sentence = o(get_case1, get_case2, get_case3)
    rule_get_sentence = Rule(attach_perperty(get_sentence, {'attribute': 'name', 'operation': 'get', 'rule': '2'}))
