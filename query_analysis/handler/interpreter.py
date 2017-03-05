#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：用户语义模板的handler
  创 建 者：余菲
  创建日期：16/9/3
"""
import tornado

from handler.base import route, BaseInnerAPIHandler
from server.server import service
from utils.utils import force_utf8_new


@route("/interpreter/info")
class Interpreter(BaseInnerAPIHandler):
    """
    用户普通语义模板的handler
    """
    def _get(self):
        """
        用户上传文本信息,取得答案
        :@param parameters:参数
        :@param robot_id:机器人ID
        @return:
        """
        speech = self.get_argument('speech')
        robot_code = self.get_argument('robot_code')
        body = service.get_semantic_info(robot_code, speech)
        body = force_utf8_new(body)
        return body


@route("/interpreter/scene_info")
class SceneInterpreter(BaseInnerAPIHandler):
    """
    用户场景语义模块的handler
    """
    def _get(self):
        """
        用户在某个场景下，上传文本信息,取得答案
        :return:
        """
        speech = self.get_argument('speech')
        robot_code = self.get_argument('robot_code')
        body = service.get_scene_semantic_info(robot_code, speech)
        body = force_utf8_new(body)
        return body

