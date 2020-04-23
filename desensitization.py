import re

f = open('C:/Users/zjk/Desktop/xml/680011.text', encoding='UTF-8-sig')
string = f.read()
f.close
# print(string)
print(re.findall(r'<姓名.*?>.*?</姓名>', string))

p1 = r'<姓名.*?>.*?</姓名>'
p2 = r'<姓名>小明</姓名>'
print(re.findall(p1, string))
# p3 = r'(?<=>).*?(?=</住址>)'
# p4 = r'火星'

# p5 = r'(?<=>).*?(?=</出生地>)'
# p6 = r'出生地月球'

# p7 = r'(?<=>).*?(?=</电话>)'
# p8 = r'010-1234567'

# p9 = r'(?<=>).*?(?=</(工作单位)>)'
# p10 = r'54所'

# p11 = r'(?<=>).*?(?=</家长姓名>)'
# p12 = r'花花'

# p13 = r'(?<=>).*?(?=</联系人姓名>)'
# p14 = r'小月月'

# p15 = r'(?<=>).*?(?=</联系人地址>)'
# p16 = r'火星'

# p15 = r'(?<=>).*?(?=</联系人电话>)'
# p16 = r'火星'

# p15 = r'(?<=>).*?(?=</籍贯省>)'
# p16 = r'北京'

# p15 = r'(?<=>).*?(?=</(联系人身份证号码|公民身份证)>)'
# p16 = r'12345677890'

p17 = r'(?<=>姓名:).*?(?=</FONT>)'
p18 = r'小月月'

p19 = r'(?<=>出生地:).*?(?=</FONT>)'
p20 = r'火星'

p21 = r'(?<=>家庭住址:).*?(?=</FONT>)'
p22 = r'水星'

newtext1 = re.sub(p1, p2, string)
# # print("替换后的文本"+newtext1)
# newtext1 = re.sub(p3, p4, string)
# newtext2 = re.sub(p3, p4, newtext1)
# # print("替换后的文本"+newtext2)
# newtext3 = re.sub(p5, p6, newtext2)
# newtext4 = re.sub(p7, p8, newtext3)
# newtext5 = re.sub(p9, p10, newtext4)
# newtext6 = re.sub(p11, p12, newtext5)
# newtext7 = re.sub(p13, p14, newtext6)
# newtext8 = re.sub(p15, p16, newtext7)
newtext9 = re.sub(p17, p18, newtext1)
newtext10 = re.sub(p19, p20, newtext9)
newtext11 = re.sub(p21, p22, newtext10)
# newtext12 = re.sub(p3, p4, newtext1)
# # newtext2 = re.sub(p3, p4, newtext1)
# # newtext2 = re.sub(p3, p4, newtext1)
# # newtext2 = re.sub(p3, p4, newtext1)
# # newtext2 = re.sub(p3, p4, newtext1)

f = open('C:/Users/zjk/Desktop/xml/sample.html','w',encoding='UTF-8-sig')
f.write(newtext11)
f.close


