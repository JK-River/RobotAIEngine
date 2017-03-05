#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：小忆语义
  创 建 者：余菲
  创建日期：16/6/19
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty

class XiaoYi(object):
    # 标识是xiaoyi领域
    service = 'xiaoyi'

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

    show = '(显示|打开|亮出|查|查询)(下)?'
    your = '(你|机器|机器人|小忆)(的)?'

    # [二维码]语义解析
    barcode = '(二维码|身份证)'
    barcode_case1 = barcode
    barcode_case2 = prefix_0_5 + show + e(your) + barcode + postfix_0_3 # 显示 二维码
    barcode_case3 = prefix_0_5 + your + barcode + postfix_0_3   # 机器人 二维码
    barcode_sentence = o(barcode_case1, barcode_case2, barcode_case3)
    rule_barcode_sentence = Rule(attach_perperty(barcode_sentence, {'attribute': 'barcode', 'operation': 'get', 'rule': 1}))

    # [软件版本]语义解析
    version = '(软件)?(版本)(号|信息)?'
    version_case1 = version
    version_case2 = prefix_0_5 + show + e(your) + version + postfix_0_3 # 显示 版本号
    version_case3 = prefix_0_5 + your + version + postfix_0_3   # 机器人 版本号
    version_sentence = o(version_case1, version_case2, version_case3)
    rule_version_sentence = Rule(attach_perperty(version_sentence, {'attribute': 'version', 'operation': 'get', 'rule': 2}))

    # [绑定状态]语义解析
    bind = '(绑定状态)'
    bind_case1 = bind
    bind_case2 = prefix_0_5 + show + e(your) + bind + postfix_0_3   # 显示 绑定状态
    bind_case3 = prefix_0_5 + your + bind + postfix_0_3 # 机器人 绑定状态
    bind_sentence = o(bind_case1, bind_case2, bind_case3)
    rule_bind_sentence = Rule(attach_perperty(bind_sentence, {'attribute': 'bind', 'operation': 'get', 'rule': 3}))

    # [网络状态]语义解析
    wifi = '(网络状态)'
    wifi_case1 = wifi   # 网络状态
    wifi_case2 = prefix_0_5 + show + e(your) + wifi + postfix_0_3   # 显示 网络状态
    wifi_case3 = prefix_0_5 + your + wifi + postfix_0_3 # 机器人 网络状态
    wifi_sentence = o(wifi_case1, wifi_case2, wifi_case3)
    rule_wifi_sentence = Rule(attach_perperty(wifi_sentence, {'attribute': 'wifi', 'operation': 'get', 'rule': 4}))
