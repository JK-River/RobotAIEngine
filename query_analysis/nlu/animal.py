#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：动物类词义
  创 建 者：余菲
  创建日期：16/5/21
"""
from dict.dict import animal_name, pronoun, stop_words, any_w, modals
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag


class Animal(object):
    # 标识是animal领域
    service = 'animal'

    animal = animal_name.join_all
    pronoun = pronoun.join_all
    stop_words = stop_words.join_all
    modals = modals.join_all

    want = '(要|想|想要)'
    query1 = '(查|查询|看|显示)(一下)?'
    query2 = '(长|什么)'
    query3 = '(样|外表|形状)'
    query4 = '(显示|找|搜索|学习|展览|展示|展出|放|表演|播|陈现|陈放|放映|给|出|画|拿)(一下)?'

    roar = '(叫|叫声)'
    append = '(加|增加|添加|加上)'
    how = '(如何|怎么)'
    call = '(是|叫)'

    animal_type = '(虫|鸟)'
    animal_type = attach_name(animal_type, 'type')
    all_animal = o(animal, animal_type)

    # 老虎(进入动物场景后，说动物名才起作用)
    case_1 = attach_perperty(all_animal, {'operation': 'query', 'rule': 1})
    rule_1 = Rule(case_1, {'status': 'animal'})

    # 老虎长什么样
    case_2 = all_animal + any_w + '({})?'.format(query2) + any_w + query3 + any_w
    case_2 = attach_perperty(case_2, {'operation': 'query', 'rule': 2})
    rule_2 = Rule(case_2)

    # 我现在想要看虫
    case_3 = e(pronoun) + e(stop_words) + want + any_w + query1 + any_w + animal_type + any_w
    case_3 = attach_perperty(case_3, {'operation': 'query', 'rule': 3})
    rule_3 = Rule(case_3)

    # 给我显示个大老虎看看
    case_4 = e(modals) + e(pronoun) + query4 + any_w + all_animal + stop_words
    case_4 = attach_perperty(case_4, {'operation': 'query', 'rule': 4})
    rule_4 = Rule(case_4)

    # 我要个大老虎看看
    case_5 = pronoun + want + any_w + all_animal + any_w
    case_5 = attach_perperty(case_5, {'operation': 'query', 'rule': 5})
    rule_5 = Rule(case_5)

    # 什么是老虎
    case_6 = query2 + call + all_animal
    case_6 = attach_perperty(case_6, {'operation': 'query', 'rule': 6})
    rule_6 = Rule(case_6)

    # 老虎怎么叫
    case_7 = any_w + all_animal + any_w + how + roar + any_w
    case_7 = attach_perperty(case_7, {'operation': 'roar', 'rule': 7})
    rule_7 = Rule(case_7)

    # 再加一只老虎
    tag = range_tag(2, 'tag')
    case_8 = e(pronoun) + e(stop_words) + append + tag + all_animal + e(stop_words)
    case_8 = attach_perperty(case_8, {'operation': 'append', 'rule': 8})
    rule_8 = Rule(case_8 + "{1,3}")


