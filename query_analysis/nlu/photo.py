#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：照片语义
  创 建 者：余菲
  创建日期：16/6/18
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, any_w
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty


class Photo(object):
    # 标识是photo领域
    service = 'photo'

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
    postfix_0_5 = r(postfix, 0, 5)

    # 拍特征词
    take = '(拍|照|合|来)'

    # 照片特征词
    photo = '(照|照片|相|相片|像|像片|影|合影)'

    # 打开特征词
    open = '(打开|开启|启动)'

    # 相机特征词
    camera = '(相机|照相机|摄像头)'

    # 不好写规则的特征表达
    take_photo = photo + photo

    # 拍照语义解析
    photo_case1 = prefix_0_5 + take + photo + postfix_0_5 # 拍照
    rule_photo_case1 = Rule(attach_perperty(r(photo_case1, 1, 3), {'operation': 'take', 'rule': 1}))

    photo_case2 = prefix_0_5 + '(把|将)?' + photo + take + postfix_0_5 # 照 拍
    rule_photo_case2 = Rule(attach_perperty(r(photo_case2, 1, 3), {'operation': 'take', 'rule': 2}))

    photo_case3 = prefix_0_5 + '(把|将)?' + photo + take + any_w + quantifier + postfix_0_5  # 拍 照；
    rule_photo_case3 = Rule(attach_perperty(r(photo_case3, 1, 3), {'operation': 'take', 'rule': 3}))

    photo_case4 = prefix_0_5 + take + any_w + quantifier + photo + postfix_0_5 # 拍 张 照；
    rule_photo_case4 = Rule(attach_perperty(r(photo_case4, 1, 3), {'operation': 'take', 'rule': 4}))

    photo_case5 = prefix_0_5 + '(拍|照)' + '(我|我们)' + postfix_0_5 # 拍我
    rule_photo_case5 = Rule(attach_perperty(r(photo_case5, 1, 3), {'operation': 'take', 'rule': 5}))

    photo_case6 = prefix_0_5 + open + camera + postfix_0_5  # 打开 相机
    rule_photo_case6 = Rule(attach_perperty(r(photo_case6, 1, 3), {'operation': 'take', 'rule': 6}))

    photo_case7 = prefix_0_5 + '(把|将)?' + camera + open + postfix_0_5    # 相机 打开
    rule_photo_case7 = Rule(attach_perperty(r(photo_case7, 1, 3), {'operation': 'take', 'rule': 7}))
