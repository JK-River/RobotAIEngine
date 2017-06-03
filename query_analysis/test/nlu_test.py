#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：语义的单元测试
  创 建 者：余菲
  创建日期：16/6/19
"""
import sys
import glob
import os
import unittest
import yaml
from unittest import main

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

os.chdir('..')

import nlu.animal as animal
import nlu.media.story as story
import nlu.media.opera as opera
import nlu.volume as volume
import nlu.expand_instruction as expand_instruction
import nlu.display as display
import nlu.mode as mode
import nlu.motion as motion
import nlu.profile as profile
import nlu.vehicle as vehichel
import nlu.sight as sight
import nlu.battery as battery
import nlu.dance as dance
import nlu.photo as photo
import nlu.entertainment as entertainment
import nlu.recognition as recognition
import nlu.xiaoyi as xiaoyi
from nlu.nlu_framework import Nlu_Framework

from utils.utils import force_utf8_new

def load_from_yaml(file_name):
    """
    从yaml加载测试信息,返回生成器
    :param file_name:
    :return:
    """
    f = open(file_name)
    return yaml.safe_load_all(f)


class Rule_Test(unittest.TestCase):
    """
    所有语义的单元测试
    """
    def setUp(self):
        print 'setUp'
        Nlu_Framework.register(animal.Animal)
        Nlu_Framework.register(battery.Battery)
        Nlu_Framework.register(dance.Dance)
        Nlu_Framework.register(display.Display)
        Nlu_Framework.register(entertainment.Entertainment)
        Nlu_Framework.register(photo.Photo)
        Nlu_Framework.register(recognition.Recognition)
        Nlu_Framework.register(xiaoyi.XiaoYi)
        Nlu_Framework.register(story.Story)
        Nlu_Framework.register(volume.Volume)
        Nlu_Framework.register(expand_instruction.ExtendInstruction)
        Nlu_Framework.register(mode.Mode)
        Nlu_Framework.register(motion.Motion)
        Nlu_Framework.register(profile.Profile)
        Nlu_Framework.register(vehichel.Vehicle)
        Nlu_Framework.register(sight.Sight)
        Nlu_Framework.register(opera.Opera)
        print 'setUp Over'

    def test_yaml(self):
        # self._generage()
        file_list = glob.glob('./test/conf/*')
        for file_name in file_list:
            print 'test' + file_name
            yaml_info_list = load_from_yaml(file_name)
            for yaml_info in yaml_info_list:
                match_dict_list = Nlu_Framework.match(force_utf8_new(yaml_info['input']))
                print yaml_info['input']
                self.assertDictEqual(force_utf8_new(match_dict_list[0]),
                                     force_utf8_new(yaml_info['output']))

    def _generage(self):
        """
        第一次产生测试yaml的方法
        :return:
        """
        file_list = glob.glob('./test/conf/*')
        for file_name in file_list:
            yaml_info_list = load_from_yaml(file_name)
            print file_name
            yaml_list = []
            for yaml_info in yaml_info_list:
                match_dict_list = Nlu_Framework.match(force_utf8_new(yaml_info['input']))
                result_dict = {"input": force_utf8_new(yaml_info['input']),
                               "output": match_dict_list[0]}
                yaml_list.append(result_dict)
            yaml_list = force_utf8_new(yaml_list)
            print yaml.safe_dump_all(yaml_list, allow_unicode=True, encoding='utf-8')

if __name__ == '__main__':
    main()
