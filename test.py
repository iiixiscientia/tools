'''
@Author: zjk
@Date: 2020-04-26 11:37:52
@LastEditTime: 2020-04-26 11:41:56
@LastEditors: zjk
@Description: 
'''

from lxml import etree
import os
import sys
import regex

def xmltohtml(inputpath, outputpath):
# convert xmlfile to html
# htmlfile = open(path, 'r', encoding='utf-8')
    
    line = os.path.split(inputpath)[1]
    line = 
    with open(inputpath, 'r', encoding='utf-8') as xmlread:
        xmltext = xmlread.read()
        # print(xmlfile)

    # 反转义
    xmlfile1 = regex.sub('&amp;','&', xmltext)
    xmlfile2 = regex.sub('&lt;','<', xmlfile1)
    xmltext = regex.sub('&gt;','>', xmlfile2)

    p1 = r'<HTML>.*?</HTML>'

    result = regex.search(p1, xmltext)
    if result:
        newtext = result[0]
    else:
        newtext = "Null"

    # save as html
    print()
    # with open('%(outputpath)%(line)+.html','w',encoding='UTF-8-sig') as f:
        # f.write(newtext)