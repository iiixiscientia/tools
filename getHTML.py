'''
@Author: zjk
@Date: 2020-04-26 09:43:48
@LastEditTime: 2020-04-26 10:55:41
@LastEditors: zjk
@Description: 读取外层xml文件并抽取内层html
'''


from lxml import etree
import os
import sys
import regex
from traverse_xml import getallfilesofwalk
from xmltohtml import xmltohtml

input_dir = "./Data1"
destination_dir = "./Data2"

path = getallfilesofwalk(input_dir)
for line in path:
    xmltohtml(line,destination_dir)

