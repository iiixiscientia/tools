    # 合并两人标注的json数据
    # 逻辑：
    # 1.读取2人的标注json数据，并遍历
    # 2.获取id值，label内容，文本内容text
    # 3.处理id值，使id范围相同
    # 4.如果id值相同，则文本1+“[SEP]” + 文本2，label内容相同的删掉，label值不同的保留
  #改： 因2此导出id值无关联，故，跟据text文本相同来合并
import json
def CombinJson(f1,f2,f3,f4):
    json_1 = open(f1, 'r', encoding='utf8')
    json_2 = open(f2, 'r', encoding='utf8')
    json_same = open(f3, 'a', encoding='utf8')
    json_diff = open(f4, 'a', encoding='utf8') #若文件存在 则写入；若不存在，则创建并写入


    labels_same = []  #用来存储labels中相同的部分
    labels_different = [] #用来存储labels中不相同的部分
    json_1_read = json_1.readlines()
    json_2_read = json_2.readlines()
    ## 读取json数据并修改id值
    for i in range(0,len(json_1_read)):
        json_data = json.loads(json_1_read[i])
        id_num = json_data["id"]  # 获取id值
        json_data["id"] = id_num - 1000
        id_num1 = json_data["id"] #修改后的id值
        text_1 = json_data["text"] #获取json_1de 文本内容
        labels_1 = json_data["labels"]  # 获取labels内容

        for k in range(0,len(json_2_read)):
            json_data2 = json.loads(json_2_read[k])
            # id_num2 = json_data2["id"]  # 获取 id值
            text_2 = json_data2["text"] #获取文件2的文本内容
            labels_2 = json_data2["labels"]  # 获取labels内容

            if text_1 == text_2:
                text = text_1 + "[SEP]" + text_2   #合并文本
                for m in labels_1:
                    if m not in labels_2:
                        labels_different.append(m)   # 获取labels_1中和labels_2不相同的标签内容
                    else:
                        labels_same.append(m)       #获取labels_1和labels_2相同的标签内容
                for n in labels_2:
                    if n not in labels_1:
                        labels_different.append(n) #获取labels_2中和labels_1不相同的标签内容
                        n[0] += len(text_2) + 5
                        n[1] += len(text_2) + 5 # 【SEP】  文本2索引需要+5

                dic_same = {"id":id_num1,"text":text_1,"labels":labels_same}  #将相同部分保留 供合并使用
                json.dump(dic_same,json_same,ensure_ascii=False) #将相同部分字典写入json文件中
                json_same.write("\n")  #写文件

                if len(labels_different) != 0:
                    dic_diff = {"id":id_num1,"text":text,"labels":labels_different}
                    json.dump(dic_diff,json_diff,ensure_ascii=False)
                    json_diff.write("\n")  #合并文本并保留不相同部分
                labels_different = []
                labels_same = []  #重置列表，避免累加
                break
            else:
                continue
    json_1.close()
    json_2.close()
    json_same.close()
    json_diff.close()

f1 = "./static/wny.json1"
f2 = "./static/xyl2.json1"
f3 = "./static/json_same.json1"
f4 ="./static/json_diff.json1"
CombinJson(f1,f2,f3,f4)  #运行函数
