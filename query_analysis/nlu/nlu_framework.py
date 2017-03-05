#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：NLU的框架类,用于支持多个领域的对象进行过滤
  创 建 者：余菲
  创建日期：16/6/4
"""
from collections import defaultdict
import regex as re

# import re2 as re
from utils.utils import get_attach_perperty
from rule import Rule


class Nlu_Framework(object):
    """
    NLU的框架类
    """
    service_map = defaultdict(list)

    word_dict_map = {}

    duplicate_key_re = re.compile(r"<([^>]*)>")

    @staticmethod
    def register(service_module):
        """
        把这个领域对象注册到NLU_框架里去
        :param service_module:
        :return:
        """
        Nlu_Framework.service_map[service_module.service] = \
            Nlu_Framework.service_init(service_module)

    @staticmethod
    def register_dict(bussiness, word_dict):
        """
        在指定语义bussiness, 下注册词典用于抓取arid的这种属性,如老虎:1
        :param bussiness: 语义名
        :param word_dict: 词典对象
        :return:
        """
        assert word_dict.group_name, "word_dict don't have group name"
        key = "{}_{}".format(bussiness, word_dict.group_name)
        Nlu_Framework.word_dict_map[key] = word_dict.property

    @staticmethod
    def service_init(service_module):
        """
        把service_module中所有Rule对象取出来,写入list
        :param service_module:
        :return: 多个re对象的list
        """
        re_list = []
        for property_name in dir(service_module):
            object_in_module = getattr(service_module, property_name)
            if not isinstance(object_in_module, (Rule, )):
                continue
            re_list.append(object_in_module)
        return re_list

    @staticmethod
    def on_status_filter(status):
        """
        按状态名进行过滤
        :param status: 状态名
        :return:
        """
        temp_rule_map = defaultdict(list)
        for service_name, rule_list in Nlu_Framework.service_map.iteritems():
            for rule in rule_list:
                if not rule.filters.get('status') == status:
                    continue
                temp_rule_map[service_name].append(rule.rule)
        return temp_rule_map

    @staticmethod
    def match(query_string, re_filter={}, re_filter_func='on_status_filter'):
        """
        检查query_string,并按注册的service,去进行解析与分析,看是否能取得一个属性dict
        :param query_string: 用于查询的query_string(我要看老虎)
        :param re_filter: 当前状态过滤函数参数
        :param re_filter_func: 过滤函数名
        :return:返回这个字符串处理后得到的属性
        """
        match_result_list = []

        # 每次过滤时重新构造需要过滤的模板，用于以后加上倒排表
        if not re_filter:
            temp_rule_map = Nlu_Framework.service_map
        else:
            filter_func = getattr(Nlu_Framework, re_filter_func)
            temp_rule_map = filter_func(**re_filter)

        for k, v in temp_rule_map.items():
            # 进入下一次的时候需要清空result_dict
            result_dict = {}
            for re_object in v:
                match_object = re_object.match(query_string)
                # 注意这里要用match_object.group(0),因为不用这个会抓前边部分数据
                if not (match_object and [m_value for m_key, m_value in match_object.groupdict().items()
                                          if m_value == query_string]):
                    continue

                # 匹配上了
                result_dict = defaultdict(dict)
                for key, math_value in match_object.groupdict().items():
                    # 去掉用于去重复而添加的三下划线___, 注意这里不去单下划线
                    key = key.replace("___", "")
                    if '__' in key and math_value:
                        result_dict.update(get_attach_perperty(key))
                    else:
                        # 多个值(a|b)时,只有命中才添加
                        if math_value:
                            result_dict.update({key: math_value})

                    # 处理值的附加属性
                    dict_attach_key = "{}_{}".format(k, key)
                    if dict_attach_key in Nlu_Framework.word_dict_map:
                        result_dict.update(Nlu_Framework.word_dict_map[dict_attach_key][math_value])
                result_dict['service'] = k
            if result_dict:
                result_dict = Nlu_Framework._format_result(result_dict)
                match_result_list.append(result_dict)
        return match_result_list

    @staticmethod
    def _format_result(result_dict):
        """
        格式化输出，只有service与operation字段在外层，其它全部放到parameters字段中
        :param result_dict:
        :return:
        """
        temp_dict = defaultdict(dict)
        for key, value in result_dict.iteritems():
            if key in ('service', 'operation'):
                temp_dict[key] = value
            else:
                temp_dict['parameters'].update({key: value})
        return temp_dict


