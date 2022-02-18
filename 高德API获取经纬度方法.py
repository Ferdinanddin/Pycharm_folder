import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}
lst = []
l1_name = []

# with open('adress.csv', 'rt', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for i, rows in enumerate(reader):
#         if i <= 28:
#             row = rows
#             lst.append(row[1])
#         if i > 29:
#             break
# del lst[0]

#
# def get_location(location):
#     gaode_api_url = "https://restapi.amap.com/v3/geocode/geo?address=" + str(location) + "&output=XML&key=key"
#     response = requests.get(gaode_api_url, headers=headers)
#     Soup = BeautifulSoup(response.content, 'lxml')
#     l1 = Soup.find('location')
#     if Soup.location == None:
#         print("查询点：{0},坐标为：{1}".format(str(location), 0))
#     else:
#         print("查询点：{0},坐标为：{1}".format(str(location), l1.text))
#     if Soup.location == None:
#         l1_name.append([str(location), 0])
#     else:
#         l1_name.append([str(location), l1.text])

# ------测试----------
# loc = "乌鲁木齐市人民政府"
# get_location(loc)
# ------测试----------


import requests
import pandas as pd
import csv
data = pd.read_csv('merge_data_modified(3.0).csv',engine='python')#导入地址的csv文件
data = data['title']#选择地址列
lis = []
def gaode(cnt):
    flag = 0
    # 写表头
    writerCsv(0,lis)

    print(len(data))

    # 遍历数据，调用接口，写数据
    for i in data:
        para = {
            'key':'507f03ab300b8aa0225a0924e7d12100',
            'address':i
            #'city':'河南省洛阳市'
        }
        url = 'https://restapi.amap.com/v3/geocode/geo?'
        req = requests.get(url,para)
        req = req.json()
        print(req)
        if req['infocode']=='10000':
            try:
                w = req['geocodes'][0]['formatted_address']
                z = req['geocodes'][0]['location']
                # print(w)
                # print(z)
                d = (i, w, z)
                lis.append(d)
                flag = flag + 1
            except Exception as e:
                print (e)
            # continue
            if flag == cnt:
                # print(lis)
                writerCsv(1, lis)
                lis.clear()
                flag = 0
            else:
                continue
    # print(lis)
    writerCsv(1,lis)
def writerCsv(flag, list):
    if flag == 0 :
        t = ['title','位置','经纬度']
        # with open('地址02_经纬度坐标.csv', 'w', newline='')as f:
        with open('nanyang_经纬度坐标.csv', 'a+', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(t)
            # writer.writerows(list)
    else:
        with open('nanyang_经纬度坐标.csv', 'a+', newline='')as f:
            writer = csv.writer(f)
            writer.writerows(list)

if __name__ == '__main__':
    gaode(30)








