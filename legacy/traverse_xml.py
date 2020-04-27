'''
@Author: zjk
@Date: 2020-04-26 10:19:05
@LastEditTime: 2020-04-26 10:58:37
@LastEditors: zjk
@Description: 批量读取xml文件
'''


# dir = "./Data1"
#使用listdir循环遍历
def getallfilesofwalk(dir):
    import os
    path = []
    if not os.path.isdir(dir):
        print(dir)
        path = dir
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            if file.endswith(".xml"):
                path.append(os.path.join(root, file))
    with open("./filename.txt", 'w', encoding='utf-8') as f:
        f.writelines(path)
    return path