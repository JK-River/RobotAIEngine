#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：打电话场景语义
  创 建 者：余菲
  创建日期：16/12/17
"""

class Phone(object):
    """
    打电话语义
    """

    def process(self, speech):
        """
        处理业务
        :param speech: 用户说的话
        :return:
        """
        relation_list = ['爸爸', '妈妈', '爷爷', '奶奶']
        for relation in relation_list:
            if relation in speech:
                return {'relation': relation}

        time_list = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for time in time_list:
            if time in speech:
                return {'time': time}
        return None

scene_phone = Phone()
