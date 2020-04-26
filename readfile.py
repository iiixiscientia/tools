'''
@Author: zjk
@Date: 2020-04-26 09:50:50
@LastEditTime: 2020-04-26 10:39:21
@LastEditors: zjk
@Description: 
'''
import os

# dir = "./Data1"


#使用listdir循环遍历
def getallfilesofwalk(dir):
    path = []
    if not os.path.isdir(dir):
        print(dir)
        path = dir
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            if file.endswith(".xml"):
                path.append(os.path.join(root, file)+'\n')
    with open("./filename.txt", 'w', encoding='utf-8') as f:
        f.writelines(path)
    return path

# out = getallfilesofwalk(dir)
# print(out)