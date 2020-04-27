'''
@Author: zjk
@Date: 2020-04-26 11:55:39
@LastEditTime: 2020-04-27 10:35:21
@LastEditors: zjk
@Description: 抽取主诉、病史、病案号等
'''
import regex
# import pandas as pd
# import numpy as np
from lxml import etree


def extract_text(file):
    
    # print(file)
    # myhtml = etree.HTML(file)
    with open(file, 'r', encoding='utf-8') as htmlfile:
        myhtml = htmlfile.read()

    # pandas数组暂存输出结果
    text = []
    # myhtml_b = bytes(bytearray(file, encoding='utf-8'))
    # myhtml = etree.HTML(myhtml)
    # result = myhtml.xpath('//*[@id="Mandala"]/table/tbody/tr[1]/td[1]/font/text()')
    # print(result)

    # 病案号
    his_record_number = r'<病案号.*?>.*?</病案号>'
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        modified_number = r'\d{6}(?=</病案号>)'
        text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    else:
        text.append('Null')


    # HIS内部标识
    medical_record_number = r'<HIS内部标识.*?>.*?</HIS内部标识>'
    medical_record_number_temp = regex.findall(medical_record_number, myhtml)
    if medical_record_number_temp:
        modified_number = r'(?<=>).*?(?=</HIS内部标识>)'
        # print("病案号：", regex.findall(modified_number, medical_record_number_temp[0]))
        text.append(regex.findall(modified_number, medical_record_number_temp[0])[0])
    else:
        # print("病案号：", "Null")
        text.append('Null')

    # # 主诉（re方法）
    # # chief_compliant = r'(?<=<STRONG>主诉.*?</STRONG>).*?(?=</FONT>)|(?<=<STRONG>主诉：</STRONG>).*?(?=</FONT>)'
    # chief_compliant = r'<P><FONT color=steelblue>.*?主诉.*?</P>'
    # chief = regex.search(chief_compliant, myhtml)
    # if chief:
    #     # remove_tag = r'<[^>]+>'
    #     # chief_no_tag = regex.sub(remove_tag,'', chief[0])
    #     # if chief_no_tag:
    #     #     chief_no_title_tag = regex.sub(r'主诉','',chief_no_tag[0])
    #     #     if chief_no_title_tag:
    #     #         text.append(chief_no_title_tag[0])
    #     from pyquery import PyQuery
    #     chief_text = PyQuery(chief[0])
    #     if chief_text.text():
    #         # clean the chief compliant text
    #         p1 = r'主诉|\n|:|：'
    #         chief_clean = regex.sub(p1,'',str(chief_text.text()))
    #         text.append(chief_clean)
    # else:
    #     text.append('Null')


    # # 现病史（re方法）
    # phpi = r'<P><FONT color=steelblue>.*?现病史.*?</P>'
    # hpi = regex.search(phpi, myhtml)
    # if hpi:
    #     # remove_tag = r'<[^>]+>'
    #     # hpi_no_tag = regex.sub(remove_tag,'', hpi[0])
    #     # if hpi_no_tag:
    #     #     hpi_no_title_tag = regex.sub(r'主诉','',hpi_no_tag[0])
    #     #     if hpi_no_title_tag:
    #     #         text.append(hpi_no_title_tag[0])
    #     from pyquery import PyQuery
    #     hpi_text = PyQuery(hpi[0])
    #     if hpi_text.text():
    #         # clean the hpi compliant text
    #         p1 = r'\n|:|：'
    #         hpi_clean = regex.sub(p1,'',str(hpi_text.text()))
    #         hpi_cut = regex.sub('.*?(?=现病史)','',hpi_clean)
    #         hpi_end = regex.sub('现病史','',hpi_cut)
    #         text.append(hpi_end)
    # else:
    #     text.append('Null')
    

    # 从主诉一直拉取到月经及婚育史（re方法）
    chiefandhistory = r'<P><FONT color=steelblue>.*?婚育史.*?</P>'
    chiefandhistory = regex.search(chiefandhistory, myhtml)
    if chiefandhistory:
        from pyquery import PyQuery
        chiefandhistory_text = PyQuery(chiefandhistory[0])
        if chiefandhistory_text.text():
            # clean the chief and history compliant text, get rid of \n,:,：
            p1 = r'\n|:|：'
            chiefandhistory_clean = regex.sub(p1,'',str(chiefandhistory_text.text()))
            if chiefandhistory_clean:

                # 拉取主诉
                chief = regex.findall(r'(?<=主诉).*?(?=现病史)',chiefandhistory_clean)
                # print(chief[0])
                if chief:
                    text.append(chief[0])
                else:
                    text.append('Null')

                # 拉取现病史
                hpi = regex.findall(r'(?<=现病史).*?(?=既往史)',chiefandhistory_clean)
                if hpi:
                    text.append(hpi[0])
                else:
                    text.append('Null')

                # 拉取既往史
                item = regex.findall(r'(?<=既往史).*?(?=个人史)',chiefandhistory_clean)
                if item:
                    text.append(item[0])
                else:
                    text.append('Null')

                # 拉取个人史
                item = regex.findall(r'(?<=个人史).*?(?=月经)',chiefandhistory_clean)
                if item:
                    text.append(item[0])
                else:
                    text.append('Null')

                # 拉取月经和婚育
                item = regex.findall(r'(?<=婚育史).*',chiefandhistory_clean)
                if item:
                    text.append(item[0])
                else:
                    text.append('Null')

            else:
                text.append('Null')
    else:
        text.append('Null')

    return text
