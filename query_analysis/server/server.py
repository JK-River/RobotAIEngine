#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：
  创 建 者：余菲
  创建日期：16/9/3
"""
from semantic_service import semantic
from utils.utils import force_utf8_new


class Server(object):
    """
    用户对话流程服务类
    """
    def get_semantic_info(self, robot_id, info):
        """
        取得用户语义信息
        @param info:
        @return:
        """
        result = semantic.semantic_info(robot_id, info)
        return result

    def get_scene_semantic_info(self, robot_id, info):
        """
        取得在指定机器人ID时，这个机器人所处场景下，返回结果
        :param robot_id: 机器人ID
        :param info: 内容
        :return:
        """
        result = semantic.scene_semantic_info(robot_id, info)
        return result

service = Server()
