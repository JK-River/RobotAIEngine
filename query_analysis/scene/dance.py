#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：跳舞的场景语义
  创 建 者：余菲
  创建日期：16/12/24
"""
import re


class Dance(object):
    """
    跳舞的场景语义
    """
    RE_OK = re.compile('(?<!不)(好|要|行)')
    RE_NO = re.compile('((?<=不)(好|要|行))|(别|算了)')

    def process(self, speech):
        """
        处理业务
        :param speech: 用户说的话
        :return:
        """
        if self.RE_OK.search(speech):
            return {"select": 'YES'}

        if self.RE_NO.search(speech):
            return {"select": 'NO'}

        # 说的话不明白,返回不知道
        else:
            return {"select": 'UNKNOW'}

sence_dance = Dance()
