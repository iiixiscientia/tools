import json
def add_accu_json(check_out_dir, same_json_dir, end_json_dir):
    """
    :param check_out_dir: 审核完后输出的json文件路径
    :param same_json_dir: 审核之前两份标注数据相同部分的文件路径
    :param end_json_dir: 得到的最后完整数据的文件路径

    审核完：审核完后的数据导出在check_out_dir，与之前相同部分的数据一一对比，将审核完后的标签数据添加进相同部分（same_json_dir），
    最后输出到end_json_dir
    开始用id值 == id值来判断相同  后发现不同次id值导出混乱，改成text == text来判断相同
    """
    f = open(check_out_dir,'r',encoding='utf-8')    # 审核完的json数据输出
    f1 = open(same_json_dir, 'r', encoding='utf-8')      # 标注完合并后相同的部分
    f2 = open(end_json_dir, 'a', encoding='utf-8')    # 将正确的部分添加进去输出新的json文件
    f3 = open("static2//error.json1", 'a', encoding='utf-8')   #
    dic_diff = {}
    f_read = f.readlines()
    f1_read = f1.readlines()

    for line1 in range(0,len(f1_read)):
        dic1 = json.loads(f1_read[line1])
        text1 = dic1['text']
        labels1 = dic1['labels']
        id_num1 = dic1["id"]

        for line in range(0,len(f_read)):
            dic = json.loads(f_read[line])
            text_dif = dic['text']
            text_split = text_dif.split("[SEP]")
            labels = dic['labels']
            id_num2 = dic["id"]

            text = text_split[0]           # 以[SEP]为分隔符分成两部分，取前一部分
            if text == text1:
                for i in range(0,len(labels1)):
                    for j in range(0,len(labels)):         # 判断审核完后输出的数据每个labels范围是否有与之前重叠的部分并打印
                        if labels[j][0]<labels1[i][0] and labels[j][1]>labels1[i][0]:
                            dic_diff = {"text":text_dif, "labels":labels}
                            print(labels[j])
                            break
                        elif labels[j][0]>=labels1[i][0] and labels[j][0]<labels1[i][1]:
                            if labels[j][0]==labels1[i][0] and labels[j][1]==labels1[i][1]:
                                continue
                            else:
                                dic_diff = {"text": text_dif, "labels": labels}
                                print(labels[j])
                            break
                #dic_out = {"text":text, "labels":labels1}
            else:
                if line == len(f_read)-1:       # 将两份标注完全相同的句子导入最后完整的数据里
                    dic_out1 = {"text": text1, "labels": labels1}
                    json.dump(dic_out1, f2, ensure_ascii=False)  # 将字典写入json文件，ensure_ascii=False：禁止输出ASCII编码
                    f2.write("\n")
                continue

            if dic_diff:
                print('error: ' + str(line))
                json.dump(dic_diff, f3, ensure_ascii=False)
                f3.write("\n")
                dic_diff = {}
                break
            else:
                labels1.extend(labels)
                dic_out1 = {"text": text1, "labels": labels1}
                json.dump(dic_out1, f2, ensure_ascii=False)  # 将字典写入json文件，ensure_ascii=False：禁止输出ASCII编码
                f2.write("\n")
                break


    f.close()
    f1.close()
    f2.close()
    f3.close()


check_out_dir = "./static2/json_data.json1"
same_json_dir = "./static2/json_same.json1"
end_json_dir = "./static2/end_data.json1"  #完整json
add_accu_json(check_out_dir, same_json_dir, end_json_dir)