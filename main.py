'''
@Author: zjk
@Date: 2020-04-26 09:43:48
@LastEditTime: 2020-04-26 21:17:37
@LastEditors: zjk
@Description: 读取外层xml文件并抽取内层html，提取主诉等内容
'''


from lxml import etree
import os
import sys
import regex
import pymysql
from traverse import gethtml, getxml
from xmltohtml import xmltohtml
from extract_text import extract_text
# import csv
# import numpy as np
# import pandas as ps

# xml files dir
input_dir = "./Data1"
# desitination html path dir
destination_dir = "./Data2"


file_xml = getxml(input_dir)


for line in file_xml:
    xmltohtml(line,destination_dir)

file_html = gethtml(destination_dir)
for file in file_html:
    # print(extract_text(file))
    with open('result.output','a+',encoding='utf-8') as f:
        output = extract_text(file)
        for item in output:
            f.write(item)
            f.write(',')
        f.write('\n')