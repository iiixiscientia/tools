'''
@Author: zjk
@Date: 2020-04-27 11:36:44
@LastEditTime: 2020-04-27 13:10:52
@LastEditors: zjk
@Description: 批量写入数据库
'''
import pymysql
from variables import workstation_host, workstation_passwd, workstation_user,workstation_port

def insert_database(index, list):
    connection = pymysql.connect(host=workstation_host,
                                 port=workstation_port,
                                 user='root',
                                 password=workstation_passwd,
                                 db='xyl',
                                 charset='utf8')
    # effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    cursor = connection.cursor()
    effect_row = cursor.execute('INSERT INTO `medical_EHR` (`HIS`, `Chief_complaint`) VALUES (%s, %s)', (list[1],list[2]))
    connection.commit()
    return effect_row

insert_database([],['123','1234','主诉'])