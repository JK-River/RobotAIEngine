#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Copyright (c) 2016,小忆机器人
  All rights reserved.

  摘    要：根据excel生成词典函数
  创 建 者：余菲
  创建日期：16/7/8
"""
import warnings
from itertools import groupby
from operator import itemgetter

from openpyxl import load_workbook

from utils.utils import force_utf8_new

warnings.simplefilter("ignore")
wb = load_workbook(filename=r'/Users/yufei/ai_svn/appidxeej8jb3bo/AI引擎/AR资源列表.xlsx')
sheet = wb['Sheet1']
content_list = []
for i in range(2, 9999):
    row_num = str(i)
    if not sheet['A'+row_num].value:
        break
    content_list.append((sheet['A' + row_num].value.replace(' ', '_'),
                         sheet['B'+row_num].value,
                         sheet['C'+row_num].value,
                         sheet['D'+row_num].value,
                         sheet['E'+row_num].value))

content_list = force_utf8_new(content_list)
content_list_temp = sorted(content_list, key=lambda x: x[3])
for item1, content_list_temp in groupby(content_list_temp, itemgetter(3)):
    print item1+":"
    content_name_list = []
    for content in content_list_temp:
        content_name_list.append(content[0])
        print "$%s{arid%s%s} = (%s);" % (content[0], '%', content[2], content[1])

    print '(' + '|'.join(["${}".format(content) for content in content_name_list]) + ')'
    print '\n\n\n'


i = 0
temp_list_id = []
content_list = sorted(content_list, key=lambda x: x[3])
for item1, item2 in groupby(content_list, itemgetter(3)):
    type_name = 'type_{}'.format(i)
    i += 1
    for subitem in item2:
        temp_list_id.append(str(subitem[2]))
        # 支持的长度,太长了讯飞语义不支持
        if len(temp_list_id) >= 40:
            break
    print '$%s{arid_list%s%s} = (%s);' % (type_name, '%',
                                    ','.join(temp_list_id),
                                    item1)
    temp_list_id = []
    temp_list_content = []

print ""
print ""

content_list = sorted(content_list, key=lambda x: x[4])
for item1, item2 in groupby(content_list, itemgetter(4)):
    if not item1:
        continue
    type_name = 'type_{}'.format(i)
    i += 1
    for subitem in item2:
        temp_list_id.append(str(subitem[2]))
        temp_list_content.append(subitem[1])
    print '$%s{arid_list%s%s} = (%s);' % (type_name, '%',
                                  ','.join(temp_list_id),
                                  item1)
    temp_list_id = []
    temp_list_content = []
