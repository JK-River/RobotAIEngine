#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：音量控制
  创 建 者：余菲
  创建日期：16/6/5
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective
from nlu.rule import Rule

from utils.utils import o, r, e, attach_perperty


class Volume(object):
    # 标识是volume领域
    service = 'volume'

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
    infix = o(prep, pronoun)

    prefix_0_5 = r(prefix, 0, 5)
    postfix_0_3 = r(postfix, 0, 3)

    # 调整特征词
    # $change_up{direction%up} = (增 | 加 | 升 | 扩)[$numeral_words] [$quantifier_words];
    change_up = '(增|加|升|扩)' + e(numeral) + e(quantifier)
    change_up = attach_perperty(change_up, {'direction': "up"})

    # $change_down{direction%down} = (减 | 降 | 缩)[$numeral_words] [$quantifier_words];
    change_down = '(减|降|缩)' + e(numeral) + e(quantifier)
    change_down = attach_perperty(change_down, {'direction': "down"})

    # $change = (调 | 调整 | 调节 | 调动 | 调理 | 调弄 | 改变 | 转变 | 弄 | 搞 | 放 | 变 | 整);
    change = '(调|调整|调节|调动|调理|调弄|改变|转变|弄|搞|放|变|整)'

    # 方向
    # $up{direction%up} = (大 | 高 | 强 | 重 | 响 | 响亮)[$numeral_words] [$quantifier_words];
    up = '(大|高|强|重|响|响亮)' + e(numeral) + e(quantifier)
    up = attach_perperty(up, {'direction': "up"})

    # $down{direction%down} = (小 | 低 | 弱 | 轻 | 低沉)[$numeral_words] [$quantifier_words];
    down = '(小|低|弱|轻|低沉)' + e(numeral) + e(quantifier)
    down = attach_perperty(down, {'direction': "down"})

    # $maximum{direction%up}{step%toend} = [(到 | 至)](最大 | 最高 | 最强 | 最重 | 最响 | 最亮);
    maximum = e('到|至') + '(最大|最高|最强|最重|最响|最亮)'
    maximum = attach_perperty(maximum, {'direction': "up", 'step': "toend"})

    # $minimum{direction%down}{step%toend} = [(到 | 至)](最小 | 最低 | 最弱 | 最轻);
    minimum = e('到|至') + '(最小|最低|最弱|最轻)'
    minimum = attach_perperty(minimum, {'direction': "down", 'step': "toend"})

    # $direction = ($up | $down | $maximum | $minimum);
    direction = o(up, down, maximum, minimum)

    # 反转的方向，用于双重否定的场景
    # $reverse_up{direction%down} = (大 | 高 | 强 | 重 | 响 | 响亮)[$numeral_words] [$quantifier_words];
    reverse_up = '(大|高|强|重|响|响亮)' + e(numeral) + e(quantifier)
    reverse_up = attach_perperty(reverse_up, {'direction': "down"})

    # $reverse_down{direction%up} = (小 | 低 | 弱 | 轻 | 低沉)[$numeral_words] [$quantifier_words];
    reverse_down = '(小|低|弱|轻|低沉)' + e(numeral) + e(quantifier)
    reverse_down = attach_perperty(reverse_down, {'direction': "up"})

    # $reverse_maximum{direction%down}{step%toend} = [(到 | 至)](最大 | 最高 | 最强 | 最重 | 最响 | 最亮);
    reverse_maximum = e('(到|至)') + '(最大|最高|最强|最重|最响|最亮)'
    reverse_maximum = attach_perperty(reverse_maximum, {'direction': "down", 'step': "toend"})

    # $reverse_minimum{direction%up}{step%toend} = [(到 | 至)](最小 | 最低 | 最弱 | 最轻);
    reverse_minimum = e('(到|至)') + '(最小|最低|最弱|最轻)'
    reverse_minimum = attach_perperty(reverse_minimum, {'direction': "up", 'step': "toend"})

    # $reverse_direction = ($reverse_up | $reverse_down | $reverse_maximum | $reverse_minimum);
    reverse_direction = o(reverse_up, reverse_down, reverse_maximum, reverse_minimum)

    # $change_case1 = ($change_up | $change_down) [$direction];
    change_case1 = o(change_up, change_down) + e(direction)
    # $change_case2 = [$change] [$degree_words] $direction;
    change_case2 = e(change) + e(degree) + direction
    # $change_case3 = (往|向|朝) [$degree_words] $direction [$change];
    change_case3 = '(往|向|朝)' + e(degree) + direction + e(change)
    # $change_direction = ($change_case1 | $change_case2 | $change_case3);
    change_direction = o(change_case1, change_case2, change_case3)

    # 音量调节特征词
    # $volume = (把|将)<0-1> [你的] (声音 | 声 | 声儿 | 音量 | 音响 | 喇叭 | 喇叭声 | 说话力气)[$numeral_words] [$quantifier_words];
    volume = r('(把|将)', 0, 1) + e('你的') + '(声音|声儿|声|音量|音响|喇叭|喇叭声|说话力气)' + e(numeral) + e(quantifier)

    # 表达方式1：大点声；小声点好吗；
    # $volume_case1 = $prefix<0-5> $change_direction $volume $postfix<0-3>;
    volume_case1 = prefix_0_5 + change_direction + volume + postfix_0_3
    rule_volume_case1 = Rule(attach_perperty(volume_case1, {'operation': 'change', 'rule': '1'}))

    # 表达方式2：声音再调大点；请你把声音调到最小可以吗；把声音调整更大一点；
    # $volume_case2 = $prefix<0-5> $volume [$infix] $change_direction $postfix<0-3>;
    volume_case2 = prefix_0_5 + volume + e(infix) + change_direction + postfix_0_3
    rule_volume_case2 = Rule(attach_perperty(volume_case2, {'operation': 'change', 'rule': '2'}))

    # 表达方式3：别那么大声；
    # $do_not = (不 | 不要 | 不想 | 不准 | 不想要 | 别);
    do_not = '(不要|不想|不准|不想要|不|别)'
    # $volume_case3 = $prefix<0-5> $do_not [$degree_words] $reverse_direction [$infix] $volume $postfix<0-3>;
    volume_case3 = prefix_0_5 + do_not + e(degree) + reverse_direction + e(infix) + volume + postfix_0_3
    rule_case3 = Rule(attach_perperty(volume_case3, {'operation': 'change', 'rule': 3}))

    # 表达方式4-9：那么大声干嘛；声音这么大干啥；干啥这么大声；
    # $why = (干嘛 | 干吗 | 干啥 |干什么 | 做什么 | 怎么 | 怎的 | 咋 | 为啥 | 为什么);
    why = '(干嘛|干吗|干啥|干什么|做什么|怎么|怎的|咋|为啥|为什么)'
    # $volume_case4 = $prefix<0-5> $why [$infix] $reverse_direction [$infix] $volume $postfix<0-3>;
    volume_case4 = prefix_0_5 + why + e(infix) + reverse_direction + e(infix) + volume + postfix_0_3
    rule_case4 = Rule(attach_perperty(volume_case4, {'operation': 'change', 'rule': 4}))

    # $volume_case5 = $prefix<0-5> $why [$infix] $volume [$infix] $reverse_direction $postfix<0-3>;
    volume_case5 = prefix_0_5 + why + e(infix) + volume + e(infix) + reverse_direction + postfix_0_3
    rule_case5 = Rule(attach_perperty(volume_case5, {'operation': 'change', 'rule': 5}))

    # $volume_case6 = $prefix<0-5> $reverse_direction [$infix] $volume [$infix] $why $postfix<0-3>;
    volume_case6 = prefix_0_5 + reverse_direction + e(infix) + volume + e(infix) + why + postfix_0_3
    rule_case6 = Rule(attach_perperty(volume_case6, {'operation': 'change', 'rule': 6}))

    # $volume_case7 = $prefix<0-5> $volume [$infix] $reverse_direction [$infix] $why $postfix<0-3>;
    volume_case7 = prefix_0_5 + volume + e(infix) + reverse_direction + e(infix) + why + postfix_0_3
    rule_case7 = Rule(attach_perperty(volume_case7, {'operation': 'change', 'rule': 7}))

    # $volume_case8 = $prefix<0-5> $reverse_direction [$infix] $why [$infix] $volume $postfix<0-3>;
    volume_case8 = prefix_0_5 + reverse_direction + e(infix) + why + e(infix) + volume + postfix_0_3
    rule_case8 = Rule(attach_perperty(volume_case8, {'operation': 'change', 'rule': 8}))

    # $volume_case9 = $prefix<0-5> $volume [$infix] $why[$infix] $reverse_direction $postfix<0-3>;
    volume_case9 = prefix_0_5 + volume + e(infix) + why + e(infix) + reverse_direction + postfix_0_3
    rule_case9 = Rule(attach_perperty(volume_case9, {'operation': 'change', 'rule': 9}))

    # 表达方式10-11：声音太大了；你说话力气好小；
    # $too_much = (太 | 过 | 过于 | 好);
    too_much = '(太|过于|过|好)'
    volume_case10 = prefix_0_5 + volume + too_much + reverse_direction + postfix_0_3
    rule_case10 = Rule(attach_perperty(volume_case10, {'operation': 'change', 'rule': 10}))

    volume_case11 = prefix_0_5 + too_much + reverse_direction + volume + postfix_0_3
    rule_case11 = Rule(attach_perperty(volume_case11, {'operation': 'change', 'rule': 11}))

    # 表达方式12：听不清楚；吵死了；你没吃饭吗；
    # $can_not_hear{direction%up} = (听不清 | 听不清楚 | 听不见 | 听不到 | 听不着 | 没吃饭);
    can_not_hear = '(听不清楚|听不清|听不见|听不到|听不着|没吃饭)'
    can_not_hear = attach_perperty(can_not_hear, {'direction': "up"})

    # $too_loud{direction%down} = (太吵 | 吵死 | 吵死人 | 吵到我 | 吃多);
    too_loud = '(太吵|吵死人|吵死|吵到我|吃多)'
    can_not_hear = attach_perperty(can_not_hear, {'direction': "down"})

    # $volume_case12 = $prefix<0-5> ($can_not_hear | $too_loud) $postfix<0-3>;
    volume_case12 = prefix_0_5 + o(can_not_hear, too_loud) + postfix_0_3
    rule_case12 = Rule(attach_perperty(volume_case12, {'operation': 'change', 'rule': 12}))

    # 表达方式13：嘘
    # $volume_case13 = (嘘 | 需 | 旭 | 徐);
    volume_case13 = '(嘘|需|旭|徐)'
    rule_case13 = Rule(attach_perperty(volume_case13, {'operation': 'change', 'rule': 13}))
