#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：管理机器人的状态
  创 建 者：余菲
  创建日期：16/10/23
"""
import json

import redis

status_redis = redis.Redis('127.0.0.1', '6549', 0, socket_timeout=2)

class RobotStatus(object):
    """
    管理机器人的状态
    """
    def __init__(self):
        pass

    @staticmethod
    def get_robot_status(robot_code):
        """
        取得robot_code的当前状态
        :param robot_code:机器人code
        :return:
        """
        status = status_redis.lindex('status_{}'.format(robot_code), 0)
        return json.loads(status) if status else None

    @staticmethod
    def set_robot_status(robot_code, status_info):
        """
        设置robot的状态
        :param robot_code: 机器人code
        :param status_info: 状态信息
        :return:
        """
        status_redis.lpush('status_{}'.format(robot_code), json.dumps(status_info))

    @staticmethod
    def clear_robot_status(robot_code):
        """
        清空robot状态
        :param robot_code:
        :return:
        """
        status_redis.delete('status_{}'.format(robot_code))