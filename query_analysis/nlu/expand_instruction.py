#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：扩展指令
  创 建 者：余菲
  创建日期：16/6/5
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb

# 标识是animal领域
from nlu.rule import Rule
from utils.utils import o, r, e, attach_perperty


class ExtendInstruction(object):
    service = 'extend_instruction'

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

    # 被中止的指令
    play = '(播放|播|说话|说|唱歌|唱|歌唱|讲故事|讲|听歌|听故事|听|跳舞|跳)'

    # 中止特征词
    do_not = '(不要|不|不想|不准|不想要|别)'
    stop = '(停一停|停一下|停止|暂停|停下|停|打住|闭嘴|安静|打断|shut up|stop)'
    get = '(知道|明白|理解|了解)'

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    # 中止语义解析
    # 请你不要播放了；别说了；
    stop_case1 = prefix_0_5 + do_not + e(degree) + play + postfix_0_3
    # 请你不要播放了；别说了；
    stop_case2 = prefix_0_5 + stop + play + postfix_0_3
    # 麻烦你停一下好吗；停停停；停啊停啊停啊
    stop_case3 = prefix_0_5 + o(stop, get) + postfix_0_3
    stop_sentence = r(o(stop_case1, stop_case2, stop_case3), 1, 3)
    rule_stop_sentence = Rule(attach_perperty(stop_sentence, {'operation': 'stop', 'rule': 1}))

    # 是语义解析：绝对正确啊；相当可以啊；挺好；对对对；
    yes = '(对|好|可以|行|正确|那还用说)'
    yes_case1 = e(adjective) + yes + r(auxiliary, 0, 3)
    yes_sentence = r(yes_case1, 1, 3)
    rule_yes_sentence = Rule(attach_perperty(yes_sentence, {'operation': 'yes', 'rule': 2}))

    # 不是语义解析：完全不对；不太行；不是很对啊；不行不行；
    not_str = '(不是|不|没|没有)'
    no_case1 = not_str + yes
    no_case2 = prefix_0_5 + not_str + e(degree) + yes + postfix_0_3
    no_sentence = r(o(no_case1, no_case2), 1, 3)
    rule_no_sentence = Rule(attach_perperty(no_sentence, {'operation': 'no', 'rule': 3}))

    # [不告诉你]语义解析：我不告诉你；不想告诉你；就不告诉你；
    tell_not = e(adverb) + "(不想|不)"
    tell = "(告诉)"
    wont_tell_case1 = prefix_0_5 + tell_not + e(degree) + tell + e(pronoun) + postfix_0_3
    rule_wont_tell_sentence = Rule(attach_perperty(wont_tell_case1, {'operation': 'wonttell', 'rule': 4}))
