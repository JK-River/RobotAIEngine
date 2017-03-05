#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：急转弯语义
  创 建 者：余菲
  创建日期：16/12/17
"""

class Trick(object):
    """
    急转弯语义
    """

    def process(self, speech):
        """
        处理业务
        :param speech: 用户说的话
        :return:
        """
        return {'speech': speech}

scene_trick = Trick()
