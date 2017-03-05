#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：语义扩展类
  创 建 者：余菲
  创建日期：16/9/3
"""
import logging

from lib.scene import RobotScene
from lib.status import RobotStatus
from nlu import animal
from nlu import battery
from nlu import dance
from nlu import display
from nlu import entertainment
from nlu import expand_instruction
from nlu import mode
from nlu import motion
from nlu import music
from nlu import phone
from nlu import photo
from nlu import profile
from nlu import recognition
from nlu import sight
from nlu import trick
from nlu import vehicle
from nlu import volume
from nlu import xiaoyi
from nlu.nlu_framework import Nlu_Framework
from nlu.media import story
from scene.scene_framework import SceneFramework
from utils.utils import force_utf8_new

Nlu_Framework.register(animal.Animal)
Nlu_Framework.register(battery.Battery)
Nlu_Framework.register(dance.Dance)
Nlu_Framework.register(display.Display)
Nlu_Framework.register(entertainment.Entertainment)
Nlu_Framework.register(photo.Photo)
Nlu_Framework.register(recognition.Recognition)
Nlu_Framework.register(xiaoyi.XiaoYi)
Nlu_Framework.register(story.Story)
Nlu_Framework.register(expand_instruction.ExtendInstruction)
Nlu_Framework.register(volume.Volume)
Nlu_Framework.register(mode.Mode)
Nlu_Framework.register(motion.Motion)
Nlu_Framework.register(profile.Profile)
Nlu_Framework.register(vehicle.Vehicle)
Nlu_Framework.register(sight.Sight)
Nlu_Framework.register(music.Music)
Nlu_Framework.register(phone.Phone)
Nlu_Framework.register(trick.Trick)

class Semantic(object):
    """
    语义扩展类
    """
    def scene_semantic_info(self, robot_code, speech):
        """
        取得场景语义信息
        1.判断是否当前机器人处理场景中，不在场景中直接返回空
        2.在场景中走指定场景语义
        :param robot_code: 机器码
        :param speech: 对话
        :return:
        """
        scene_name = RobotScene.get_scene_name(robot_code)
        logging.warn(scene_name)
        if not scene_name:
            logging.error('no scene, robot_code:%s, speech:%s', robot_code, speech)
            return None

        match_info = SceneFramework.process(scene_name, robot_code, speech)
        self._update_robot_status(robot_code, match_info['service'])
        return match_info

    def semantic_info(self, robot_code, speech):
        """
        取得普通的语义信息
        :param robot_code: 机器码
        :param speech: 对话
        :return:
        """
        match_dict_list = Nlu_Framework.match(force_utf8_new(speech))
        logging.warn(match_dict_list)
        if not match_dict_list:
            current_status = RobotStatus.get_robot_status(robot_code)
            logging.warn(current_status)
            match_dict_list = Nlu_Framework.match(force_utf8_new(speech), {'status': current_status})
            logging.warn(match_dict_list)

        assert len(match_dict_list) <= 1, 'match_dict_list len great than 1'

        # 没命中语义,走其它逻辑
        if not match_dict_list:
            return None

        # 语义信息
        match_info = match_dict_list[0]

        # 注意：如果包含场景信息，则需要在语义阶段修改机器人的场景信息
        self._update_scene(robot_code, match_info)
        self._update_robot_status(robot_code, match_info['service'])
        return match_info

    def _update_scene(self, robot_code, match_info):
        """
        根据语义的信息，来更新scene信息
        需要考虑场景是否变更，如果发现场景发现了变更，则要清空之前的场景信息
        :param robot_code: 机器码
        :param match_info: 语义信息
        :return:
        """
        import logging
        if 'scene' not in match_info.get('parameters'):
            return

        old_scene_name = RobotScene.get_scene_name(robot_code)
        scene_name = match_info['parameters']['scene']
        if old_scene_name != scene_name:
            RobotScene.clear_scene_name(robot_code)
            logging.warn('new %s', scene_name)
            RobotScene.set_scene_name(robot_code, scene_name)

        # 支持场景转移的子场景信息
        if 'sub_scene' not in match_info['parameters']:
            return

        RobotScene.set_scene_kv(robot_code, 'sub_scene', match_info['parameters']['sub_scene'])

    def _update_robot_status(self, robot_code, status):
        """
        更新机器人状态
        :param robot_code: 机器码
        :param status: 状态
        :return:
        """
        RobotStatus.set_robot_status(robot_code, status)

semantic = Semantic()
