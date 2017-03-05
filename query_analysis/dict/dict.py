#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：配置信息,用于加载所有词典信息
  创 建 者：余菲
  创建日期：16/5/21
"""

class WordsDict(object):
    """
    用于判断词语的Words
    """
    prefix = ''
    suffix = ''

    def __init__(self, file_name, property_name_list=None,
                 group_name=None, prefex='', suffix=''):
        """
        用于加载csv文件, 取得文件的属性,来初始化word列表
        :param file_name: 文件名
        :param property_name_list: 属性列表
        :param group_name: 分组名
        :return:
        """
        self.words_list = []
        self.property = {}
        self.group_name = group_name
        self.prefix = prefex
        self.suffix = suffix

        if not property_name_list:
            self.load_from_file(file_name, group_name)
            return

        self.load_from_file_with_perperty(file_name,
                                          property_name_list,
                                          group_name)

    def load_from_file(self, file_name, group_name=None):
        """
        从文件中直接加载词典,只有词,没有属性
        :param file_name:
        :param group_name:
        :return:
        """
        with open(file_name) as f:
            self.words_list = [line.strip().replace('\n', '') for line in f]
        self.group_name = group_name

    def load_from_file_with_perperty(self, file_name, property_name_list, group_name):
        """
        从文件中加载词典,有词有属性
        :param file_name:
        :param property_name_list:
        :param group_name:
        :return:
        """
        property = {}
        words_list = []
        with open(file_name, 'rU') as f:
            for line in f:
                array = line.strip().split(',')
                if not array:
                    continue
                words_list.append(array[0])
                property[array[0]] = dict(zip(property_name_list, array[1:]))
        self.words_list = words_list
        self.property = property
        self.group_name = group_name

    @property
    def join_all(self):
        """
        返回用于正则表达式的词列表(老虎|兔子),或返回用于命中与捕捉的带名字指定的块
        :return: (老虎|兔子), (?P<name>老虎|兔子)
        """
        if not self.group_name:
            result = '({}{}{})'.format(self.prefix, '|'.join(self.words_list), self.suffix)
            return result
        else:
            result = '(?P<{}>({}{}{}))'.format(self.group_name, self.prefix, '|'.join(self.words_list), self.suffix)
            return result

    def set_group_name(self, group_name):
        """
        设置当前dict的group_name
        :param group_name: 分组名
        :return:
        """
        self.group_name = group_name

# 注意group_name中不能出现下划线
animal_name = WordsDict(
    './dict/animal/animal.csv',
    property_name_list=['arid'],
    group_name='animal')

# 注意group_name中不能出现下划线
opera_name = WordsDict(
    './dict/opera/opera.csv',
    property_name_list=['type'],
    group_name='opera')

story_name = WordsDict(
    './dict/story/story.csv',
    group_name='story')

vehicle_name = WordsDict(
    './dict/vehicle/vehicle.csv',
    property_name_list=['arid'],
    group_name='vehicle')

sight_name = WordsDict(
    './dict/sight/sight.csv',
    property_name_list=['arid'],
    group_name='sight')

stop_words = WordsDict('./dict/common/stop_words.csv')
pronoun = WordsDict('./dict/common/pronoun.csv')
adverb = WordsDict('./dict/common/adverb.csv')
modals = WordsDict('./dict/common/modals.csv')
prep = WordsDict('./dict/common/prep.csv')
degree = WordsDict('./dict/common/degree.csv')
honorific = WordsDict('./dict/common/honorific.csv')
interj = WordsDict('./dict/common/interj.csv')
auxiliary = WordsDict('./dict/common/auxiliary.csv')
quantifier = WordsDict('./dict/common/quantifier.csv')
numeral = WordsDict('./dict/common/numeral.csv')
adjective = WordsDict('./dict/common/adjective.csv')
directional = WordsDict('./dict/common/directional.csv')
prefix_unsual = WordsDict('./dict/common/prefix_unsual.csv')

any_w = '(.)*'

from nlu.nlu_framework import Nlu_Framework
Nlu_Framework.register_dict('animal', animal_name)
Nlu_Framework.register_dict('opera', opera_name)
Nlu_Framework.register_dict('vehicle', vehicle_name)
Nlu_Framework.register_dict('sight', sight_name)
