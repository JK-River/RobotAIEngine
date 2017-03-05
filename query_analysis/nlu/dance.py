#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：舞蹈语义
  创 建 者：余菲
  创建日期：16/6/19
"""

from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, any_w
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty, attach_name


class Dance(object):
    # 标识是dance领域
    service = 'dance'

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
    infix_0_2 = r(infix, 0, 2)

    # 修饰动作的副词
    hurry = '(快|快点|赶紧|赶快)'

    # 跳舞特征词，日志中有多个唱舞蹈的表述特此增加
    move = e(hurry) + '(跳|来|唱)' + e(numeral) +e(quantifier)
    dance = e('把|将') + '(舞|舞蹈|跳舞)'
    see = '(看|看看|观看|查看|瞧|瞅|瞄|观赏|欣赏)' + e(quantifier)
    postures = e(adjective) + '(舞姿|舞蹈)'

    # 舞蹈名称、类型、标签
    dance_name = '(杰克逊|小苹果|生日快乐)'

    dance_type1 = '机械舞'
    dance_type2 = '街舞'
    dance_type3 = '芭蕾舞'
    dance_type4 = '现代舞'
    dance_type5 = '国标舞'
    dance_type6 = '摩登舞'
    dance_type7 = '华尔兹'
    dance_type8 = '探戈'
    dance_type9 = '狐步'
    dance_type10 = '快步'
    dance_type11 = '维也纳华尔兹'
    dance_type12 = '拉丁舞'
    dance_type13 = '伦巴'
    dance_type14 = '恰恰恰'
    dance_type15 = '桑巴'
    dance_type16 = '斗牛'
    dance_type17 = '牛仔舞'
    dance_type18 = '民族舞'
    dance_type19 = '扇子舞'
    dance_type20 = '秧歌'
    dance_type21 = '手绢花'
    dance_type22 = '伞舞'
    dance_type23 = '孔雀舞'
    dance_type24 = '竹竿舞'
    dance_type25 = '儿童舞'
    dance_type26 = '丝带舞'
    dance_type27 = '踢踏舞'
    dance_type28 = '爵士舞'
    dance_type29 = '钢管舞'
    dance_type30 = '广场舞'

    dance_type1 = attach_perperty(dance_type1, {'type': 1})
    dance_type2 = attach_perperty(dance_type2, {'type': 2})
    dance_type3 = attach_perperty(dance_type3, {'type': 3})
    dance_type4 = attach_perperty(dance_type4, {'type': 4})
    dance_type5 = attach_perperty(dance_type5, {'type': 5})
    dance_type6 = attach_perperty(dance_type6, {'type': 6})
    dance_type7 = attach_perperty(dance_type7, {'type': 7})
    dance_type8 = attach_perperty(dance_type8, {'type': 8})
    dance_type9 = attach_perperty(dance_type9, {'type': 9})
    dance_type10 = attach_perperty(dance_type10, {'type': 10})
    dance_type11 = attach_perperty(dance_type11, {'type': 11})
    dance_type12 = attach_perperty(dance_type12, {'type': 12})
    dance_type13 = attach_perperty(dance_type13, {'type': 13})
    dance_type14 = attach_perperty(dance_type14, {'type': 14})
    dance_type15 = attach_perperty(dance_type15, {'type': 15})
    dance_type16 = attach_perperty(dance_type16, {'type': 16})
    dance_type17 = attach_perperty(dance_type17, {'type': 17})
    dance_type18 = attach_perperty(dance_type18, {'type': 18})
    dance_type19 = attach_perperty(dance_type19, {'type': 19})
    dance_type20 = attach_perperty(dance_type20, {'type': 20})
    dance_type21 = attach_perperty(dance_type21, {'type': 21})
    dance_type22 = attach_perperty(dance_type22, {'type': 22})
    dance_type23 = attach_perperty(dance_type23, {'type': 23})
    dance_type24 = attach_perperty(dance_type24, {'type': 24})
    dance_type25 = attach_perperty(dance_type25, {'type': 25})
    dance_type26 = attach_perperty(dance_type26, {'type': 26})
    dance_type27 = attach_perperty(dance_type27, {'type': 27})
    dance_type28 = attach_perperty(dance_type28, {'type': 28})
    dance_type29 = attach_perperty(dance_type29, {'type': 29})
    dance_type30 = attach_perperty(dance_type30, {'type': 30})

    dance_type = o(dance_type1, dance_type2, dance_type3, dance_type4, dance_type5, dance_type6,
                   dance_type7, dance_type8, dance_type9, dance_type10, dance_type11, dance_type12,
                   dance_type13, dance_type14, dance_type15, dance_type16, dance_type17,
                   dance_type18, dance_type19, dance_type20, dance_type21, dance_type22,
                   dance_type23, dance_type24, dance_type25, dance_type26, dance_type27,
                   dance_type28, dance_type29, dance_type30)

    # 其他不好写规则的特征表达
    dance_unusual = '(来到舞蹈)'

    # 舞蹈语义解析
    dance_case1 = prefix_0_5 + move + dance + postfix_0_3 # 跳 舞
    rule_dance_case1 = Rule(attach_perperty(r(dance_case1, 1, 3), {'operation': 'action', 'rule': 1}))
    dance_case2 = prefix_0_5 + dance + move + postfix_0_3 # 舞 来
    rule_dance_case2 = Rule(attach_perperty(r(dance_case2, 1, 3), {'operation': 'action', 'rule': 2}))
    dance_case3 = prefix_0_5 + move + dance_name + '(的)?' + e(dance) + postfix_0_3  # 跳 小苹果
    rule_dance_case3 = Rule(attach_perperty(r(dance_case3, 1, 3), {'operation': 'action', 'rule': 3}))
    dance_case4 = prefix_0_5 + dance_name + '(的)?' + e(dance) + move + postfix_0_3  # 小苹果 来
    rule_dance_case4 = Rule(attach_perperty(r(dance_case4, 1, 3), {'operation': 'action', 'rule': 4}))
    dance_case5 = prefix_0_5 + move + dance_type + e(dance) + postfix_0_3   # 跳 机械舞
    rule_dance_case5 = Rule(attach_perperty(r(dance_case5, 1, 3), {'operation': 'action', 'rule': 5}))
    dance_case6 = prefix_0_5 + dance_type + e(dance) + move + postfix_0_3   # 机械舞 来
    rule_dance_case6 = Rule(attach_perperty(r(dance_case6, 1, 3), {'operation': 'action', 'rule': 6}))
    dance_case7 = prefix_0_5 + see + '(你(的)?)' + postures + postfix_0_3     # 看 你的 舞姿
    rule_dance_case7 = Rule(attach_perperty(r(dance_case7, 1, 3), {'operation': 'action', 'rule': 7}))
    dance_case8 = prefix_0_5 + dance + '(你)?' + modals + move + postfix_0_3   # 舞 会不会 跳
    rule_dance_case8 = Rule(attach_perperty(r(dance_case8, 1, 3), {'operation': 'action', 'rule': 8}))
    dance_case9 = postfix_0_3 + dance_unusual + postfix_0_3 # 特殊规则
    rule_dance_case9 = Rule(attach_perperty(r(dance_case9, 1, 3), {'operation': 'action', 'rule': 9}))

    # 跳舞场景
    dance_case10 = '(小忆)?你会跳舞吗'
    rule_dance_case10 = Rule(attach_perperty(dance_case10, {'operation': 'action', 'rule': 10, 'scene': 'dance', 'node': 'query'}))

    # 跳舞场景
    dance_case11 = '(小忆)?你会跳什么舞'
    rule_dance_case11 = Rule(attach_perperty(dance_case11, {'operation': 'action', 'rule': 11, 'scene': 'dance', 'node': 'get'}))
