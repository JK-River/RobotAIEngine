#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：
  创 建 者：余菲
  创建日期：16/12/17
"""
import json

import redis

scene_redis = redis.Redis('127.0.0.1', '6579', 0, socket_timeout=2)

class RobotScene(object):
    """
    管理机器人的场景
    """
    def __init__(self):
        pass

    @staticmethod
    def get_scene(robot_code):
        """
        取得robot_code的当前场景与场景详情
        :param robot_code:机器人code
        :return:
        """
        scene = scene_redis.hgetall(robot_code)
        return scene

    @staticmethod
    def set_scene_name(robot_code, scene_name):
        """
        设置机器人的场景
        :param robot_code: 机器人code
        :param scene_name: 场景名
        :return:
        """
        scene_redis.hset(robot_code, 'name', scene_name)

    @staticmethod
    def get_scene_name(robot_code):
        """
        取得当前机器人的场景名
        :param robot_code: 机器人code
        :return:
        """
        return scene_redis.hget(robot_code, 'name')

    @staticmethod
    def clear_scene_name(robot_code):
        """
        清空场景名
        :param robot_code: 机器码
        :return:
        """
        scene_redis.delete(robot_code)

    @staticmethod
    def set_scene_kv(robot_code, key, value):
        """
        设置机器人的场景kv对
        :param robot_code: 机器人code
        :param key: key
        :param value: value
        :return:
        """
        scene_redis.hset(robot_code, key, value)

    @staticmethod
    def get_scene_kv(robot_code, key):
        """
        取得机器人的场景指定KV对
        :param robot_code: 机器人code
        :param key: key
        :return:
        """
        return scene_redis.hget(robot_code, key)

