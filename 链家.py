
# -*- encoding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from lxml import etree
import csv
import random


USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

USER_AGENT = random.choice(USER_AGENT_LIST)

#
f = open("链家main.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
headers = {
    'Cookie':'lianjia_uuid=c1479879-1663-4173-8ca1-f47cd670824f; _ga=GA1.2.1832236604.1637113221; UM_distinctid=17d2b8d54cd81-0ff25fbf1c59f-57b193e-144000-17d2b8d54cec1f; _smt_uid=61945dff.1904f43f; sensorsdata2015jssdkcross={"distinct_id":"17d2b8d3e15f3-09a1b3581b396a-57b193e-1327104-17d2b8d3e16886","$device_id":"17d2b8d3e15f3-09a1b3581b396a-57b193e-1327104-17d2b8d3e16886","props":{"$latest_traffic_source_type":"直接流量","$latest_referrer":"","$latest_referrer_host":"","$latest_search_keyword":"未取到值_直接打开"}}; select_city=310000; lianjia_ssid=06a9e4ae-5650-4365-ade1-5db471dcb98f; crosSdkDT2019DeviceId=-jmdi1d--2s8wtc-ridjgkt92kimzix-z48e85y5x; login_ucid=2000000074068069; lianjia_token=2.001491dba26a70862b053cf293a7a15440; lianjia_token_secure=2.001491dba26a70862b053cf293a7a15440; security_ticket=D8OXHbr2Dwu47STcQlnX5PwMpd4NPMfdd0Bb7ycxeOdrRAYZZVaRhZVarS0Y739iFl1pykOs+BFqrnkaqfrtjTqXc8umjRkbjsBlgCewA7wNOsfYh7Xu5d9YLs5rGbWhqLwwVlWOnhlwLuCIf39O2IrwflB0eVP/xq0hS3XbN6k=; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1642644640; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1642644640; CNZZDATA1253492439=336599855-1637105084-https%3A%2F%2Fwww.google.com%2F|1642637299; CNZZDATA1254525948=656484595-1637112738-https%3A%2F%2Fwww.google.com%2F|1642634365; CNZZDATA1255633284=690895053-1637109541-https%3A%2F%2Fwww.google.com%2F|1642634285; CNZZDATA1255604082=965785922-1637112965-https%3A%2F%2Fwww.google.com%2F|1642634009; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMTZhOTgzN2I0MjYwZmY5NGQ2YjJkOGZmNTMxNDY1NjMxZDI3NDM1ODM5NjUxMWExOWY1NzJiZmU4MzkzZGIwMDVkYjJlMTk4YjAzYjI4YWQ4YTExNDc0ZTY0ZDZiY2JkZDAxYTkyMDg2ZTQ0NjM2OGI0N2EyNDZiNGQ0YWI2Njc0NWIyYzZmMGMxNDAyNjgzN2Q3NTYxMzRiOGJhNDNkMmIwODNjNzc4NmExN2ViNWJmZmI0ZWQ0MzA4MTg3OTgyYmY1NTQwM2FmYTJlYjA5NjI2MWJmNDlkYjliMDU2MTcyMmI4M2ZiMjJiNDNhZmYxMzJlYmY1ZjgyMTU3MDA0ZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3NTcxODM0Y1wifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL2NoZW5namlhby9tdzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _jzqa=1.3509370299358932000.1637113343.1639321709.1642644642.4; _jzqc=1; _jzqx=1.1637113343.1642644642.2.jzqsr=google.com|jzqct=/.jzqsr=clogin.lianjia.com|jzqct=/; _jzqckmp=1; _qzja=1.698330837.1637113344676.1639321709653.1642644642948.1639321846008.1642644642948.0.0.0.18.4; _qzjc=1; _qzjto=1.1.0; _jzqb=1.1.10.1642644642.1; _qzjb=1.1642644642948.1.0.0.0; _gid=GA1.2.634050289.1642644646; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
url = 'https://sh.lianjia.com/chengjiao/pudong/pg3pr4/'
resp = requests.get(url, headers=headers)
html = etree.HTML(resp.text)
page = html.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/span/text()")
print(resp.text)

regions = ['pudong', 'minhang', 'baoshan', 'xuhui', 'putuo', 'yangpu', 'songjiang', 'jiading', 'huangpu', 'jingan', 'hongkou','qingpu', 'fengxian', 'jinshan', 'chongming', 'shanghaizhoubian']
prices = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
for re in regions:
    for pr in prices:
        page = 1
        url = 'https://sh.lianjia.com/chengjiao/' + re + '/pg' + str(page) + pr + '/'
        resp = requests.get(url, headers=headers)
        html = etree.HTML(resp.text)
        uls = html.xpath("/html/body/div[5]/div[1]/ul")
        for dl in uls:
            title = dl.xpath("./li/div/div[1]/a/text()")
            price = dl.xpath("./li/div/div[2]/div[3]/span/text()")
            age = dl.xpath("./li/div/div[3]/div[1]/text()")
            unit_price = dl.xpath("./li/div/div[3]/div[3]/span/text()")
            time = dl.xpath("./li/div/div[2]/div[2]/text()")
            for s in range(len(title)):
                property.append([title[s], age[s], price[s], unit_price[s], time[s]])
                csvwriter.writerows(property)
        if page >= html.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/span/text()")[0]:
            break
        page = page + 1
        print("region: " + re + ", price: " + pr + ', page: ' + str(page))



# for i in range(2, 101):
#    meanUrl = f"https://sh.lianjia.com/chengjiao/{i}"
#    meanPage = requests.get(meanUrl, headers=headers)
#    print("页面状态码:{0}".format(meanPage.status_code))
#    soup = BeautifulSoup(meanPage.text, "html.parser")
#    tag = soup.find_all("script")[3]
#    a = str(tag).find("rfss")
#    var_t4 = meanUrl
#    var_t3 = str(tag)[a:a + 28]
#    newUrl = var_t4 + "?" + var_t3
#    print("当前访问为 {0}:".format(newUrl))
#    newPage = requests.get(newUrl, headers=headers)
#
#    # newSoup = BeautifulSoup(newPage.text, "html.parser")
#
#
#    html = etree.HTML(newPage.text)
#    dls = html.xpath("/html/body/div[3]/div[6]/div[3]")
#    for dl in dls:
#       title = dl.xpath("./dl/dd/p[1]/a/text()")
#       title = [item.replace("\n", "").replace("\t", "") for item in title]
#       district = dl.xpath("./dl/dd/p[3]/a[1]/text()")
#       detail_district = dl.xpath("./dl/dd/p[3]/a[2]/text()")
#       price = dl.xpath("./dl/dd/div[3]/p[1]/span[1]/text()")
#       unit_price = dl.xpath("./dl/dd/div[3]/p[2]/b/text()")
#       time = dl.xpath("./dl/dd/div[2]/p[1]/text()")



      # for s in range(len(title)):
      #    list = [title[s], face[s], district[s],detail_district[s], price[s], unit_price[s], time[s]]
      #    values.append(list)
      #    csvwriter.writerows(values)




      # csvwriter.writerow(title)
      # csvwriter.writerow(face)



   # 拿到每一个tr
   # for tr in trs:
   #    t1 = tr.xpath("./td/text()")
   #    t2 = tr.xpath("./td/span/text()")
   #    # 对数据进行简单的处理
   #    t = t1 + t2
   #    # 把数据存放在文件中
   #    csvwriter.writerow(t)
# #print(newSoup)
# fangData = []
# attrs = ["户型", "面积", "楼层", "朝向", "建成时间", "经纪人", "地址", "单价"]
# df = pd.DataFrame(columns=attrs)
#
# print(newDf)
