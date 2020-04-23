#coding=utf-8

# from bs4 import BeautifulSoup
# import xml.etree.ElementTree as ET
import regex
import os
import sys

# path = 'C:/Users/zjk/Desktop/xml/422.html'
path = './chief_compliant.html'

htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

# chief = r'<FONT.*?>.*?</FONT>'
chief_compliant = r'(?<=<FONT color=#000000><STRONG>主诉:</STRONG>).*?(?=</FONT>)'
past_history = r'(?<=<FONT color=#000><STRONG>既往史：</STRONG>).*?(?=</FONT>)'
personal_history = r'(?<=<FONT color=#000><STRONG>&nbsp;个人史:</STRONG>).*?(?=</FONT>)'
current_medical_history = r'(?<=<FONT color=#000><STRONG>现病史:</STRONG>).*?(?=</FONT>)'
family_medical_history = r'(?<=<FONT color=#000><STRONG>&nbsp;家族史:</STRONG>).*?(?=</FONT>)'
menstruation_and_marriage_history = r'<FONT color=#000000><STRONG>月经及婚育史.*?</STRONG>.*?(?=</FONT>)'

print("主诉：", regex.findall(chief_compliant, htmlhandle))
print("既往史：", regex.findall(past_history, htmlhandle))
print("个人史：", regex.findall(personal_history, htmlhandle))
print("现病史：", regex.findall(current_medical_history, htmlhandle))
print("家族史：", regex.findall(family_medical_history, htmlhandle))

# print("月经及婚史：", regex.findall(menstruation_and_marriage_history, htmlhandle))

modified = regex.findall(menstruation_and_marriage_history, htmlhandle)[0]
print(modified)
modified_reg = r'(?<=</STRONG>).*'
print("月经及婚史：", regex.findall(modified_reg, modified))
