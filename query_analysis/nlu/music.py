#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：音乐语义
  创 建 者：余菲
  创建日期：16/9/24
"""

from dict.dict import story_name, pronoun, adverb, modals, stop_words, honorific, any_w
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag

class Music(object):
    # 标识是music领域
    service = 'music'

    story_name = story_name.join_all
    stop_words = stop_words.join_all
    pronoun = pronoun.join_all
    can_words = modals.join_all
    adverb = adverb.join_all
    ask = honorific.join_all
    give = '(给)'
    want = '(要|想要|想|需要)'

    # 语义意图，仅支持一种，播放
    listen = '(听|来)(一)?(首)?'
    sing = '(唱|播放|播|来|看)'

    # 音乐人名
    artist = range_tag(4, 'artist')

    # 音乐名
    music_name = range_tag(8, 'song')

    # 音乐的说法
    music = '(音乐|儿歌|歌曲|歌)'

    # robot
    robot = '(你|机器人|小忆)'

    # me
    me = '(我|我们|咱|咱们|俺)'

    # 再，又
    again = '(再|又|多)'

    # 首
    an = e('(首|一首)')

    # 你唱
    you_sing = robot + sing

    # 听音乐
    case_1 = e(me) + e(want) + e(again) + e(adverb) + listen + e(you_sing) \
             + o(an) + o(music, music_name) + e(stop_words)
    case_2 = e(me) + e(want) + e(again) + e(adverb) + listen + e(you_sing) \
             + e(artist) + e('的') + music_name
    case_3 = sing + music_name

    # (给我)唱首xxx的歌
    case_4 = e(give) + e(me) + sing + an + artist + '的歌'

    # rule_1 = Rule(attach_perperty(case_1, {'operation': 'play', 'rule': 1}))
    # rule_2 = Rule(attach_perperty(case_2, {'operation': 'play', 'rule': 2}))
    # rule_3 = Rule(attach_perperty(case_3, {'operation': 'play', 'rule': 3}))
    rule_4 = Rule(attach_perperty(case_4, {'operation': 'play', 'rule': 3}))
