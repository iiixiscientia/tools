'''
@Author: zjk
@Date: 2020-04-24 18:49:32
@LastEditTime: 2020-04-25 23:47:42
@LastEditors: zjk
@Description: 读取外层xml文件并抽取第二层xml
'''


from lxml import etree
import os
import sys
import regex


path = '422.xml'

# htmlfile = open(path, 'r', encoding='utf-8')
with open(path, 'r', encoding='utf-8') as xmlread:
    
    xmltext = xmlread.read()
    # print(xmlfile)

# 反转义
xmlfile1 = regex.sub('&amp;','&', xmltext)
xmlfile2 = regex.sub('&lt;','<', xmlfile1)
xmltext = regex.sub('&gt;','>', xmlfile2)

path = r'<HTML>.*?</HTML>'

result = regex.search(path, xmltext)
if result:
    newtext = result[0]
else:
    newtext = "Null"

# save as html
with open('./Data1/test.html','w',encoding='UTF-8-sig') as f:
    f.write(newtext)


# myxml = bytes(bytearray(xmltext, encoding='utf-8'))
# myxml = etree.XML(myxml)

# result = etree.tostring(myxml,pretty_print = True,encoding = "utf-8")
# # print(result.decode('utf-8'))
# # print(myxml.tag)

# result = myxml.xpath('//*')
# print(result)

# /html/body/p[31]/font[2]

# 用xpath的方法获取主诉
myhtml = etree.HTML(newtext)
result = myhtml.xpath('/html/body/p[31]/font[2]/text()')
print(result)