'''
@Author: zjk
@Date: 2020-04-26 09:43:48
@LastEditTime: 2020-04-27 12:54:01
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
from ToDatabase import *
from tqdm import tqdm
# import csv
# import numpy as np
# import pandas as ps

# xml files dir
input_dir = "C:\\Users\\13438\\PycharmProjects\\data\\extradata\\Data1"
# desitination html path dir
destination_dir = "C:\\Users\\13438\\PycharmProjects\\data\\extradata\\Data2"
index = 0

file_xml = getxml(input_dir)

# for line in file_xml:
#     xmltohtml(line,destination_dir)

file_html = gethtml(destination_dir)

i = 0
for file in tqdm(file_html):
    item_list = extract_text(file)
    index = index + 1

    #insert_database(index, item_list)

    try:
        insert_database(index, item_list)
    except:
        i = i + 1
        print('insert error : HIS id is ' + item_list[1])

print('error num : ' + str(i))
connection.close()
    
    # with open('result.output','a+',encoding='utf-8') as f:
    #     output = extract_text(file)
    #     for item in output:
    #         f.write(item)
    #         f.write(',')
    #     f.write('\n')
