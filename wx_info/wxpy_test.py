import re
from wxpy import *
import numpy
import pandas as pd
import matplotlib.pyplot as plt
# 参考https://blog.csdn.net/yaoyefengchen/article/details/79427475
def login():
    bot = Bot(cache_path=None)
    my_friends = bot.friends()
    print(type(my_friends))
    return my_friends

# 机器人账号自身
#myself = bot.self

# 向文件传输助手发送消息1111
bot.file_helper.send('Hello from wxpy!')


#统计好友男女比例
def show_sex_ratio(friends):
    sex_dict = {'male': 0, 'female': 0}
    for frient in my_friends:
        if frient.sex == 1:
            sex_dict['male'] += 1
        elif frient.sex == 2:
            sex_dict['female'] += 1
    print(sex_dict)
#保持登陆/运行
# 进入 Python 命令行、让程序保持运行
#embed()

#写入txt文本
def write_txt_file(path , txt):
    with open(path, 'a', encoding='gb18030',newline='') as f:
        f.write(txt)

def read_txt_file(path):
    with open(path,'r', encoding='gb18030', newline='') as f:
        return f.read()

def show_area_distribution(friends):
    # 使用一个字典统计各省好友数量
    province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
        '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
        '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
        '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
        '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
        '四川': 0, '贵州': 0, '云南': 0,
        '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
        '香港': 0, '澳门': 0}

    # 统计省份
    for friend in friends:
        if friend.province in province_dict.keys():
            province_dict[friend.province] += 1

    # 为了方便数据的呈现，生成JSON Array格式数据
    data = []
    for key, value in province_dict.items():
        data.append({'name': key, 'value': value})

    print(data)

#统计好友签名
def show_signature(friends):
    for friend in friends:
        # 对数据进行清洗，将标点符号等对词频统计造成影响的因素剔除
        pattern = re.compile(r'[一-龥]+')
        filterdata = re.findall(pattern, friend.signature)
