#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：播放类的语义父模块（相声，故事，戏剧）
  创 建 者：余菲
  创建日期：17/2/25
"""
from dict.dict import pronoun, modals, prep, degree, honorific, interj, \
    auxiliary, quantifier, numeral, adjective, adverb, prefix_unsual, any_w, stop_words

from utils.utils import o, r, e, range_tag

pronoun = pronoun.join_all
modals = modals.join_all
prep = prep.join_all
degree = degree.join_all
honorific = honorific.join_all
interj = interj.join_all
prefix_unsual = prefix_unsual.join_all
auxiliary = auxiliary.join_all
quantifier = quantifier.join_all
numeral = numeral.join_all
adjective = adjective.join_all
adverb = adverb.join_all
stop_words = stop_words.join_all
want = '(要|想要|想|需要)'

prefix = o(pronoun, prep, modals, degree, honorific, interj, prefix_unsual)
postfix = o(auxiliary, prep, pronoun)
infix = o(prep, pronoun, degree)

prefix_0_5 = r(prefix, 0, 5)
postfix_0_3 = r(postfix, 0, 3)

# 语义意图，仅支持一种，播放
see = '(听|看)' + e('一') + e('个')
tell = '(讲|说|播放|播|来|看|打开)' + e('一') + e('个|段')

# 不能明确理解语义的限定词，统一归类到TAG
tag = range_tag(12, 'tag')

# robot
robot = '(你|机器人|小忆)'

# me
me = '(我|我们|咱|咱们|俺)'

# 再，又
again = '(再|又|多)'

# ask
ask = '(请|让|叫|要|要求|麻烦)'

# give
give = '(给|对|帮忙|帮助|帮|为)'

# can
can = '(能|可以)'

# 你讲
you_say = robot + tell
