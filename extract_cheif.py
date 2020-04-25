#coding=utf-8

# from bs4 import BeautifulSoup
# import xml.etree.ElementTree as ET
import regex
import os
import sys

regex.purge()

# path = 'C:/Users/zjk/Desktop/xml/422.html'
path = 'C:/Users/zjk/Desktop/xml/Data1/00090036.xml'

# htmlfile = open(path, 'r', encoding='utf-8')
xmlread = open(path, 'r', encoding='utf-8')
xmlfile = xmlread.read()

# 反转义
xmlfile1 = regex.sub('&amp;','&', xmlfile)
xmlfile2 = regex.sub('&lt;','<', xmlfile1)
xmlfile3 = regex.sub('&gt;','>', xmlfile2)

htmlhandle = xmlfile3

f = open('./Data1/test.xml','w',encoding='UTF-8-sig')
f.write(xmlfile3)
f.close

## process the html file


# chief = r'<FONT.*?>.*?</FONT>'
chief_compliant = r'(?<=<STRONG>主诉:</STRONG>).*?(?=</FONT>)|(?<=<STRONG>主诉：</STRONG>).*?(?=</FONT>)'
past_history = r'(?<=<STRONG>既往史：</STRONG>).*?(?=</FONT>)|(?<=<STRONG>既往史:</STRONG>).*?(?=</FONT>)'
personal_history = r'(?<=<STRONG>&nbsp;个人史:</STRONG>).*?(?=</FONT>)|(?<=<STRONG>&nbsp;个人史：</STRONG>).*?(?=</FONT>)'
current_medical_history = r'(?<=<STRONG>现病史:</STRONG>).*?(?=</FONT>)|(?<=<STRONG>现病史:</STRONG>).*?(?=</FONT>)'
# family_medical_history = r'(?<=<STRONG>&nbsp;家族史:</STRONG>).*?(?=</FONT>)|(?<=<STRONG>&nbsp;家族史：</STRONG>).*?(?=</FONT>)'
family_medical_history = r'(?<=家族史:</STRONG>).*?(?=</FONT>)|(?<=家族史：</STRONG>).*?(?=</FONT>)'
menstruation_and_marriage_history = r'<STRONG>月经及婚育史.*?</STRONG>.*?(?=</FONT>)'


medical_record_number = r'<病案号.*?>.*?</病案号>'
medical_record_number_temp = regex.findall(medical_record_number, htmlhandle)
if medical_record_number_temp:
    modified_number = r'\d{6}(?=</病案号>)'
    print("病案号：", regex.findall(modified_number, medical_record_number_temp[0]))
else:
    print("病案号：", "Null")


print("主诉：", regex.findall(chief_compliant, htmlhandle))
print("既往史：", regex.findall(past_history, htmlhandle))
print("个人史：", regex.findall(personal_history, htmlhandle))
print("现病史：", regex.findall(current_medical_history, htmlhandle))
print("家族史：", regex.findall(family_medical_history, htmlhandle))
# print("月经及婚史1：", regex.findall(menstruation_and_marriage_history, htmlhandle))


modified = regex.findall(menstruation_and_marriage_history, htmlhandle)
# print(modified)
if modified:
    modified_reg = r'(?<=</STRONG>).*?(?<=</STRONG>).*'
    print("月经及婚史：", regex.findall(modified_reg, modified[0]))
else:
    print("月经及婚史：", "Null")
