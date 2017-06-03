#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：个人信息
  创 建 者：余菲
  创建日期：16/6/11
"""
from dict.dict import pronoun, stop_words, any_w, modals
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, r, range_tag, range_not_tag


class Profile(object):
    # 标识是profile领域
    service = 'profile'

    pronoun = pronoun.join_all
    stop_words = stop_words.join_all
    modals = modals.join_all

    me = '(我|俺|咱)'
    me = attach_perperty(me, {'subject': 'user'})
    your = '(你)'
    your = attach_perperty(your, {'subject': 'robot'})
    person = o(me, your)

    ti_ch_0_3 = range_tag(3, start=0)

    what = '(什么|几|多少|啥)'
    what_name = '(什么|啥)'
    know = '(知道|清楚|明白|了解|知不知道|知道不知道|搞清楚|看|说)'
    name = '(名字|名称|名|称呼)'
    name = attach_perperty(name, {'attribute': 'name'})

    age = '(年级|年龄|岁)'
    age = attach_perperty(age, {'attribute': 'age'})

    man = '(男|男生|男人|帅哥|男同学)'
    man = attach_perperty(man, {'gender': 1})

    woman = '(女|女生|女人|美女|女同学)'
    woman = attach_perperty(woman, {'gender': 2})
    gender = o(man, woman)

    strange_relation = range_tag(4)
    strange_relation = attach_name(strange_relation, 'relationDesc')
    strange_relation = attach_perperty(strange_relation, {'relationid': 99, 'closeReletive': 'no'})

    relationid_0 = '(小){0,1}主人'
    relationid_0 = attach_perperty(relationid_0, {'relationid': 0, 'closeReletive': 'yes'})

    relationid_1 = '(爸爸|老豆|老爸)'
    relationid_1 = attach_perperty(relationid_1, {'relationid': 1, 'closeReletive': 'yes'})

    relationid_2 = '(妈妈|老妈|妈)'
    relationid_2 = attach_perperty(relationid_2, {'relationid': 2, 'closeReletive': 'yes'})

    relationid_3 = '(爷爷|祖父)'
    relationid_3 = attach_perperty(relationid_3, {'relationid': 3, 'closeReletive': 'yes'})

    relationid_4 = '(奶奶|祖母)'
    relationid_4 = attach_perperty(relationid_4, {'relationid': 4, 'closeReletive': 'yes'})

    relationid_5 = '(姥姥|外婆|外祖母)'
    relationid_5 = attach_perperty(relationid_5, {'relationid': 5, 'closeReletive': 'yes'})

    relationid_6 = '(姥爷|外公|外祖父)'
    relationid_6 = attach_perperty(relationid_6, {'relationid': 6, 'closeReletive': 'yes'})

    relationid_7 = '(哥哥|哥)'
    relationid_7 = attach_perperty(relationid_7, {'relationid': 7, 'closeReletive': 'yes'})

    relationid_8 = '(弟弟|弟)'
    relationid_8 = attach_perperty(relationid_8, {'relationid': 8, 'closeReletive': 'yes'})

    relationid_9 = '(姐姐|姐)'
    relationid_9 = attach_perperty(relationid_9, {'relationid': 9, 'closeReletive': 'yes'})

    relationid_10 = '(妹妹|妹)'
    relationid_10 = attach_perperty(relationid_10, {'relationid': 10, 'closeReletive': 'yes'})

    relationid_11 = '(伯伯|叔叔)'
    relationid_11 = attach_perperty(relationid_11, {'relationid': 11, 'closeReletive': 'no'})

    relationid_12 = '(伯母|婶婶)'
    relationid_12 = attach_perperty(relationid_12, {'relationid': 12, 'closeReletive': 'no'})

    relationid_13 = '(姑姑)'
    relationid_13 = attach_perperty(relationid_13, {'relationid': 13, 'closeReletive': 'no'})

    relationid_14 = '(姑父|姑丈)'
    relationid_14 = attach_perperty(relationid_14, {'relationid': 14, 'closeReletive': 'no'})

    relationid_15 = '(舅舅|舅公)'
    relationid_15 = attach_perperty(relationid_15, {'relationid': 15, 'closeReletive': 'no'})

    relationid_16 = '(舅妈|舅母)'
    relationid_16 = attach_perperty(relationid_16, {'relationid': 16, 'closeReletive': 'no'})

    relationid_17 = '(姨姨|姨|姨妈)'
    relationid_17 = attach_perperty(relationid_17, {'relationid': 17, 'closeReletive': 'no'})

    relationid_18 = '(姨夫|姨丈)'
    relationid_18 = attach_perperty(relationid_18, {'relationid': 18, 'closeReletive': 'no'})

    relationid_19 = '(堂哥|堂弟|表哥|表弟)'
    relationid_19 = attach_perperty(relationid_19, {'relationid': 19, 'closeReletive': 'no'})

    relationid_20 = '(堂姐|堂妹|表姐|表妹)'
    relationid_20 = attach_perperty(relationid_20, {'relationid': 20, 'closeReletive': 'no'})

    relation = o(relationid_0, relationid_1, relationid_2, relationid_3, relationid_4, relationid_5,
                 relationid_6, relationid_7, relationid_8, relationid_9, relationid_10, relationid_11,
                 relationid_11, relationid_12, relationid_13, relationid_14, relationid_15, relationid_16,
                 relationid_17, relationid_18, relationid_19, relationid_20)
    relation = attach_name(relation, 'relationDesc')

    master = '(小主人|他|你)'
    slave = '(你|机器人|小忆)'

    real_name = range_tag(3, 'name')
    real_age = range_not_tag(2, what, 'age')

    # 我叫什么名字
    query_name1 = person + '(叫)' + what + name
    query_name1 = attach_perperty(query_name1, {'attribute': 'name', 'rule': 'queryName1'})
    rule_query_name1 = Rule(attach_perperty(query_name1, {'operation': 'get'}))

    # 我几岁
    query_age1 = person + '(今年|现在)?' + what + '岁'
    query_age1 = attach_perperty(query_age1, {'attribute': 'age', 'rule': 'queryName1'})
    rule_query_age1 = Rule(attach_perperty(query_age1, {'operation': 'get'}))

    # 你知道我的名字吗
    query_name2 = ti_ch_0_3 + slave + ti_ch_0_3 + know + person + ti_ch_0_3 + name + e(stop_words)
    query_name2 = attach_perperty(query_name2, {'attribute': 'name', 'rule': 'queryName2'})
    rule_query_name2 = Rule(attach_perperty(query_name2, {'operation': 'get'}))

    # 你知道我叫什么吗
    query_name3 = ti_ch_0_3 + slave + ti_ch_0_3 + know + person + ti_ch_0_3 + '叫' + what_name + e(name) + e(stop_words)
    query_name3 = attach_perperty(query_name3, {'attribute': 'name', 'rule': 'queryName3'})
    rule_query_name3 = Rule(attach_perperty(query_name3, {'operation': 'get'}))

    # 你几岁
    query_age2 = ti_ch_0_3 + slave + ti_ch_0_3 + what + age + e(stop_words)
    query_age2 = attach_perperty(query_age2, {'rule': 'query_age2'})
    rule_query_age2 = Rule(attach_perperty(query_age2, {'operation': 'get'}))

    # 你多大
    query_age3 = ti_ch_0_3 + person + ti_ch_0_3 + '(多大)' + e('(年龄|年纪)') + e(stop_words)
    query_age3 = attach_perperty(query_age3, {'rule': 'query_age3', 'attribute': 'age'})
    rule_query_age3 = Rule(attach_perperty(query_age3, {'operation': 'get'}))

    # 你看我多大了
    query_age4 = ti_ch_0_3 + slave + know + person + '(多大)' + e('(年龄|年纪)') + e(stop_words)
    query_age4 = attach_perperty(query_age4, {'rule': 'query_age4', 'attribute': 'age'})
    rule_query_age4 = Rule(attach_perperty(query_age4, {'operation': 'get'}))

    # 你知道我是谁吗(我是谁)
    query_relation1 = ti_ch_0_3 + e(slave) + e(know) + person + ti_ch_0_3 + '(谁)' + e(stop_words)
    query_relation1 = attach_perperty(query_relation1, {'attribute': 'relation', 'rule': 'queryRelation1'})
    rule_query_relation1 = Rule(attach_perperty(query_relation1, {'operation': 'get'}))

    # 你知道我的性别？
    query_gender1 = ti_ch_0_3 + slave + ti_ch_0_3 + know + person + ti_ch_0_3 + '(性别|男女|是男是女|男的女的)' + e(stop_words)
    query_gender1 = attach_perperty(query_gender1, {'attribute': 'gender', 'rule': 'queryGender1'})
    rule_query_gender1 = Rule(attach_perperty(query_gender1, {'operation': 'get'}))

    # 我是男是女？
    query_gender2 = ti_ch_0_3 + person + ti_ch_0_3 + '(性别|男女|是男是女)' + e(stop_words)
    query_gender2 = attach_perperty(query_gender2, {'attribute': 'gender', 'rule': 'queryGender2'})
    rule_query_gender2 = Rule(attach_perperty(query_gender2, {'operation': 'get'}))

    # 我叫XX
    answer_name = ti_ch_0_3 + person + ti_ch_0_3 + "(叫)" + real_name
    answer_name = attach_perperty(answer_name, {'rule': 'answerName'})
    rule_answer_name = Rule(attach_perperty(answer_name, {'operation': 'answer'}))

    # 我XX岁
    answer_age = ti_ch_0_3 + person + e('(今年|现在)') + real_age + '岁' + e(stop_words)
    # answer_age = ti_ch_0_3 + person + e('(今年|现在)') + real_age + '岁' + e(stop_words)
    answer_age = attach_perperty(answer_age, {'rule': 'answerAge'})
    rule_answer_age = Rule(attach_perperty(answer_age, {'operation': 'answer'}))

    # 我是男/女的
    answer_gender = ti_ch_0_3 + person + '(是|就是)' + gender + e(stop_words)
    answer_gender = attach_perperty(answer_gender, {'rule': 'answerGender'})
    rule_answer_gender = Rule(attach_perperty(answer_gender, {'operation': 'answer'}))

    # 我是小主人的xx
    answer_relation_1 = ti_ch_0_3 + person + '(是|就是)' + master + '(的)' + relation + e(stop_words)
    answer_relation_1 = attach_perperty(answer_relation_1, {'rule': 'answerRelation1'})
    rule_answer_relation_1 = Rule(attach_perperty(answer_relation_1, {'operation': 'answer'}))

    # 我是小主人/爸爸
    answer_relation_2 = ti_ch_0_3 + person + '(是|就是)' + relation
    answer_relation_2 = attach_perperty(answer_relation_2, {'rule': 'answerRelation2'})
    rule_answer_relation_2 = Rule(attach_perperty(answer_relation_2, {'operation': 'answer'}))

    # # 我是小主人的三爷爷
    # answer_relation_3 = person + '(就是|是)' + o('你|小忆|机器人|小主人') + ('(的)') + strange_relation
    # answer_relation_3 = attach_perperty(answer_relation_3, {'rule': 'answerRelation3'})
    # rule_strange_relation_3 = Rule(attach_perperty(answer_relation_3, {'operation': 'answer'}))
