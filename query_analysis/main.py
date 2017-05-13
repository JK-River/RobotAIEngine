#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：
  创 建 者：余菲
  创建日期：16/6/4
"""
import re
import time

import nlu.animal as animal
import nlu.battery as battery
import nlu.dance as dance
import nlu.display as display
import nlu.entertainment as entertainment
import nlu.expand_instruction as expand_instruction
import nlu.mode as mode
import nlu.motion as motion
import nlu.photo as photo
import nlu.profile as profile
import nlu.recognition as recognition
import nlu.media.story as story
import nlu.sight as sight
import nlu.vehicle as vehichel
import nlu.volume as volume
import nlu.xiaoyi as xiaoyi
import nlu.media.opera as opera
import nlu.store_location as store_location
from nlu import music
from nlu import phone
from nlu import trick
from nlu import vehicle

from nlu.nlu_framework import Nlu_Framework

# Nlu_Framework.register(animal.Animal)
# Nlu_Framework.register(battery.Battery)
# Nlu_Framework.register(dance.Dance)
# Nlu_Framework.register(display.Display)
# Nlu_Framework.register(entertainment.Entertainment)
# Nlu_Framework.register(photo.Photo)
# Nlu_Framework.register(recognition.Recognition)
# Nlu_Framework.register(xiaoyi.XiaoYi)
# Nlu_Framework.register(story.Story)
# Nlu_Framework.register(expand_instruction.ExtendInstruction)
# Nlu_Framework.register(volume.Volume)
# Nlu_Framework.register(mode.Mode)
# Nlu_Framework.register(motion.Motion)
Nlu_Framework.register(profile.Profile)
# Nlu_Framework.register(vehicle.Vehicle)
# Nlu_Framework.register(sight.Sight)
# Nlu_Framework.register(music.Music)
# Nlu_Framework.register(phone.Phone)
# Nlu_Framework.register(trick.Trick)
# Nlu_Framework.register(store_location.StoreLocation)

# def load_from_file(file_name):
#     """
#     从文件中直接加载词典,只有词,没有属性
#     :param file_name:
#     :param group_name:
#     :return:
#     """
#     with open(file_name) as f:
#         test_list = [line.strip().replace('\n', '') for line in f if line and not line.startswith('=')]
#     return test_list
#
# test_list = load_from_file('./test/test.csv')
#
#
#
#
# import yaml
# # list1 = []
# # for test_sentence in test_list:
# #     match_dict_list = Nlu_Framework.match(test_sentence)
# #     # print str(test_sentence)
# #     dict1 = {"input": test_sentence,
# #              "output": match_dict_list[0]}
# #     list1.append(dict1)
# #     # print force_utf8_new(match_dict_list[0])
# #
# #
# # list1 = force_utf8_new(list1)
# #
# # print yaml.safe_dump_all(list1, allow_unicode=True, encoding='utf-8')
# f = open('./test/test.yaml')
# input = yaml.safe_load_all(f)
# for i in input:
#     print force_utf8_new(i)

# print 'start'
# a = time.time()
# for i in range(1000):
match_dict_list = Nlu_Framework.match('小忆我告诉你手机放在椅子上')
print match_dict_list[0]['parameters']['object']
# b = time.time()
# print a - b
# print match_dict_list


# a = re.match('(小忆我问你)(?P<object>(.)+?)(放在|在)(哪里|什么地方|什么位置)', '小忆我问你手机放在哪里').groups()
# for i in a:
#     print i