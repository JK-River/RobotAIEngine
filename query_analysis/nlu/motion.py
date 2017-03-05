#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：动作语义
  创 建 者：余菲
  创建日期：16/6/11
"""
from dict.dict import pronoun, stop_words, any_w, modals
from nlu.rule import Rule
from utils.utils import attach_perperty, attach_name, o, e, range_tag

class Motion(object):
    # 标识是motion领域
    service = 'motion'

    pronoun = pronoun.join_all
    stop_words = stop_words.join_all
    modals = modals.join_all

    robot = '(你|机器人|小忆)'
    ask = '(请|让|要|要求|麻烦)'
    word1 = '(将|把)'

    up = '(抬头|抬起头|看|抬起来)'
    up = attach_perperty(up, {'code': 'lookUp', 'emotion': 12})
    down = '(低头|低下头|低个头|向下|低下去)'
    down = attach_perperty(down, {'code': 'lookDown', 'emotion': 10})
    shake = '(摇头|摇下头|摇个头|转头)'
    shake = attach_perperty(shake, {'code': 'shakeHead', 'emotion': 8})
    nod = '(点(下|个)?头)'
    nod = attach_perperty(nod, {'code': 'nod', 'emotion': 21})
    twist = '(扭下|扭个|动下|动个)'
    twist = attach_perperty(twist, {'code': 'twist', 'emotion': 12})
    stand = "站(直|好|稳|住|定)"
    stand = attach_perperty(stand, {'code': 'stand', 'emotion': 12})

    run = '跑{1,2}'
    run = attach_perperty(run, {'operation': 'run'})
    fly = '飞{1,2}'
    fly = attach_perperty(fly, {'operation': 'fly'})
    jump = '跳{1,2}'
    jump = attach_perperty(jump, {'operation': 'jump'})
    swim = '游{1,2}'
    swim = attach_perperty(swim, {'operation': 'swim'})
    turn = '转{1,2}'
    turn = attach_perperty(turn, {'operation': 'turn'})

    move = o(run, fly, jump, swim, turn)

    fast = '(全速|快点|快)'
    fast = attach_perperty(fast, {'speed': 'fast'})
    slow = '(慢速|慢点|缓慢|慢)'
    slow = attach_perperty(slow, {'speed': 'slow'})
    speed = o(fast, slow)

    will = '(向|朝)'

    dirction_1 = '上'
    dirction_1 = attach_perperty(dirction_1, {'direction': 'up'})
    dirction_2 = '下'
    dirction_2 = attach_perperty(dirction_2, {'direction': 'down'})
    dirction_3 = '前'
    dirction_3 = attach_perperty(dirction_3, {'direction': 'forth'})
    dirction_4 = '后'
    dirction_4 = attach_perperty(dirction_4, {'direction': 'back'})
    dirction_5 = '左'
    dirction_5 = attach_perperty(dirction_5, {'direction': 'left'})
    dirction_6 = '右'
    dirction_6 = attach_perperty(dirction_6, {'direction': 'right'})
    dirction = o(dirction_1, dirction_2, dirction_3, dirction_4, dirction_5, dirction_6)
    dirction = e(will) + dirction

    # 快向上看
    action_sentence1 = e(robot) + e(speed) + e(dirction) + o(up, down, shake, nod, twist) + e(stop_words)
    action_sentence1 = attach_perperty(action_sentence1, {'operation': 'action', 'rule': 1})

    # 请将头抬起来
    action_sentence2 = e(robot) + e(ask) + e(robot) + e(word1) + e('头') + o(up, down, shake, nod, twist) + e(stop_words)
    action_sentence2 = attach_perperty(action_sentence2, {'operation': 'action', 'rule': 2})

    # 快X呀
    move_sentence1 = e(speed) + move + e(stop_words)
    move_sentence1 = attach_perperty(move_sentence1, {'rule': 3})

    # 你X
    move_sentence2 = e(modals) + e(pronoun) + move + e(stop_words)
    move_sentence2 = attach_perperty(move_sentence2, {'rule': 4})

    # 快点向左转
    action = o(run, fly, jump, swim, turn)
    action_sentence3 = e(ask) + e(robot) + e(speed) + e(will) + e(stop_words) + dirction + e(stop_words) + action + e(stop_words)
    action_sentence3 = attach_perperty(action_sentence3, {'rule': 5})

    # 转快点
    action_sentence4 = e(ask) + e(robot) + action + e(speed) + e(stop_words)
    action_sentence4 = attach_perperty(action_sentence4, {'rule': 6})

    # 站直了
    action_sentence5 = e(ask) + e(robot) + stand + e(speed) + e(stop_words)
    action_sentence5 = attach_perperty(action_sentence5, {'rule': 7})

    rule_case1 = Rule(o(action_sentence1, action_sentence2))
    rule_case2 = Rule(action_sentence3)
    rule_case3 = Rule(action_sentence4)
    rule_case4 = Rule(o(move_sentence1, move_sentence2))
    rule_case5 = Rule(action_sentence5)

