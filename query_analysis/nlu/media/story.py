#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：故事类语义
  创 建 者：余菲
  创建日期：16/6/5
"""
from dict.dict import story_name, pronoun, adverb, modals, stop_words, honorific, any_w
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag


class Story(object):
    # 标识是story领域
    service = 'story'

    story_name = story_name.join_all
    stop_words = stop_words.join_all
    pronoun = pronoun.join_all
    can_words = modals.join_all
    adverb = adverb.join_all
    ask = honorific.join_all
    want = '(要|想要|想|需要)'

    # 语义意图，仅支持一种，播放
    listen = '(听|看)(一)?(个)?'
    tell = '(讲|说|播|播放|来|看)(一)?(个|段)?'

    # 故事分类
    story_type = '(童话|寓言|神话|传奇|成语|睡前|名人|益智|历史|民间|爱国|人物|动物|儿童小说|战争)'
    story_type = attach_name(story_type, 'genre')

    # 不故道名字的故事
    unknow_story_name = range_tag(6, 'unknow_story_name') + "的"

    # 不能明确理解语义的限定词，统一归类到TAG
    tag = range_tag(12, 'tag')

    # 故事的感觉
    sence = '(幽默|讽刺)'
    sence = attach_name(sence, 'sence')

    # 故事适合的听众
    audience = '(儿童|3岁|4岁|5岁|6岁|7岁|8岁)'
    audience = attach_name(audience, 'audience')

    # 故事的说法，包含这些词的会被归类到故事语义
    story = '(故事|寓言|童话)'

    # 直接说故事名称
    title_case = o(listen, tell) + story_name + stop_words;

    # robot
    robot = '(你|机器人|小忆)'

    # me
    me = '(我|我们|咱|咱们|俺)'

    # 再，又
    again = '(再|又|多)'

    # 个
    an = e('个|一个')

    # 你讲
    you_say = robot + tell

    # 听故事
    case_1 = e(me) + e(want) + e(again) + e(adverb) + listen + e(you_say) \
        + o(story, story_name) + e(stop_words)
    case_2 = e(me) + e(want) + e(again) + e(adverb) + listen + e(you_say) \
        + o(story_type, sence, audience, story_name) + e('的') + story + any_w
    case_3 = e(me) + e(want) + e(again) + e(adverb) + listen + e(you_say) \
        + tag + e('的') + story_name + any_w

    # 故事我要听
    case_4 = story_name + me + e(want) + listen

    # 我能请你给我讲故事
    case_5 = e(me) + e(can_words) + e(ask) + e(robot) + e(adverb) + e('来') \
        + e('给') + e(me) + e(again) + tell + an \
        + o(story, story_name) + any_w

    case_6 = e(me) + e(can_words) + e(ask) + e(robot) + e(adverb) + e('来') \
        + e('给') + e(me) + e(again) + tell + an \
        + any_w + o(story_type, sence, audience, story_name, unknow_story_name) + e('的') \
        + story + any_w

    # 你会讲小红帽的故事吗
    case_8 = e(robot) + e(can_words) + e(adverb) + e('给') + e(me) + e(again) \
        + tell + an + e(o(story_type, sence, audience, story_name, unknow_story_name)) \
        + e('的') + story + any_w

    # 小红帽的故事你会讲吗
    case_9 = story_name + e('的') + e(story) + e(robot) + e(can_words) + e(tell) + e(stop_words)

    # 小红帽的故事给我讲吧
    case_10 = story_name + e('的') + e(story) + e(ask) + e('为|给') + e(me) \
        + tell + e(stop_words)

    # 那讲个故事吧
    case_11 = e(can_words) + e('请') + tell + '(个|一个)' \
        + o(story_type, sence, audience, story_name) + any_w

    # 不好听 换个故事
    case_12 = any_w + e(robot) + e(adverb) + '(换|变|再找)' \
        + an + e(tag) + e(story_type) + e('的') + story + any_w

    rule_1 = Rule(attach_perperty(case_1, {'operation': 'play', 'rule': 1}))
    rule_2 = Rule(attach_perperty(case_2, {'operation': 'play', 'rule': 2}))
    rule_3 = Rule(attach_perperty(case_3, {'operation': 'play', 'rule': 3}))
    rule_4 = Rule(attach_perperty(case_4, {'operation': 'play', 'rule': 4}))
    rule_5 = Rule(attach_perperty(case_5, {'operation': 'play', 'rule': 5}))
    rule_6 = Rule(attach_perperty(case_6, {'operation': 'play', 'rule': 6}))
    rule_8 = Rule(attach_perperty(case_8, {'operation': 'play', 'rule': 8}))
    rule_9 = Rule(attach_perperty(case_9, {'operation': 'play', 'rule': 9}))
    rule_10 = Rule(attach_perperty(case_10, {'operation': 'play', 'rule': 10}))
    rule_11 = Rule(attach_perperty(case_11, {'operation': 'play', 'rule': 11}))
    rule_12 = Rule(attach_perperty(case_12, {'operation': 'play', 'rule': 12}))
