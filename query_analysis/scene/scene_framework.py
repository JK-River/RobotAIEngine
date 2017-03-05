#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：基于场景的语义信息提取框架类
  创 建 者：余菲
  创建日期：16/12/17
"""
import logging

from scene.dance import sence_dance
from scene.phone import scene_phone
from scene.trick import scene_trick


class SceneFramework(object):

    scene_map = {}

    @classmethod
    def register(cls, scene_name, scene):
        """
        把scene类注册到框架中
        :param scene_name: 场景名
        :param scene: 场景处理类
        :return:
        """
        cls.scene_map[scene_name] = scene

    @classmethod
    def process(cls, scene_name, robot_code, speech):
        """
        处理输入语句
        :param scene_name: 场景名
        :param speech: 输入语句
        :return:
        """
        if scene_name not in cls.scene_map:
            raise Exception('scene %s not register' % scene_name)

        logging.warn(scene_name)

        if scene_name not in cls.scene_map:
            logging.error('scene not support: %s, %s', scene_name, speech)
            return None

        result = cls.scene_map[scene_name].process(speech)

        # 添加状态信息,用于在框架使用
        result['service'] = scene_name
        return result

SceneFramework.register('phone_call', scene_phone)
SceneFramework.register('dance', sence_dance)
SceneFramework.register('trick', scene_trick)

