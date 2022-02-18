# -*- encoding:utf-8 -*-
import requests
from lxml import etree
import random
import csv
from concurrent.futures import ThreadPoolExecutor
import time
f = open("链家transaction_information.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
USER_AGENT_LIST = [
     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
    'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
    ]

USER_AGENT = random.choice(USER_AGENT_LIST)

headers = {
    'cookie': 'lianjia_uuid=c1479879-1663-4173-8ca1-f47cd670824f; _ga=GA1.2.1832236604.1637113221; UM_distinctid=17d2b8d54cd81-0ff25fbf1c59f-57b193e-144000-17d2b8d54cec1f; _smt_uid=61945dff.1904f43f; sensorsdata2015jssdkcross={"distinct_id":"17d2b8d3e15f3-09a1b3581b396a-57b193e-1327104-17d2b8d3e16886","$device_id":"17d2b8d3e15f3-09a1b3581b396a-57b193e-1327104-17d2b8d3e16886","props":{"$latest_traffic_source_type":"直接流量","$latest_referrer":"","$latest_referrer_host":"","$latest_search_keyword":"未取到值_直接打开"}}; crosSdkDT2019DeviceId=-jmdi1d--2s8wtc-ridjgkt92kimzix-z48e85y5x; select_city=310000; login_ucid=2000000074068069; _jzqckmp=1; _jzqx=1.1637113343.1642969286.4.jzqsr=google.com|jzqct=/.jzqsr=clogin.lianjia.com|jzqct=/; _gid=GA1.2.2086335511.1642969291; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1642644640,1642969285,1643039761; CNZZDATA1253492439=336599855-1637105084-https%3A%2F%2Fwww.google.com%2F|1643037275; CNZZDATA1254525948=656484595-1637112738-https%3A%2F%2Fwww.google.com%2F|1643033972; CNZZDATA1255633284=690895053-1637109541-https%3A%2F%2Fwww.google.com%2F|1643033891; CNZZDATA1255604082=965785922-1637112965-https%3A%2F%2Fwww.google.com%2F|1643033613; _qzjc=1; _jzqa=1.3509370299358932000.1637113343.1642969286.1643039763.9; _jzqc=1; lianjia_ssid=73433be9-fb93-44c1-86fe-96d2d27c3273; lianjia_token=2.0013d630286d376da1027b1919eb212cf4; lianjia_token_secure=2.0013d630286d376da1027b1919eb212cf4; security_ticket=D+6L4KvgkJYc5r99bwtJ5QZtLTys2Suz3XZCIyuj9S0Y6QrxK35FkNiwKI1za4aXzGzDtaEHSovi8ffHfKm8IZ3R/pYO9uzwV0FOGk0Y9aAHS8toZVyWUjyySHKxvcCvZ75m7fo1SfWXZGE790sfJkLrmTmJlsxrd2UbwB89kzs=; _jzqb=1.6.10.1643039763.1; _qzja=1.698330837.1637113344676.1642969287279.1643039762662.1643040905771.1643040985690.0.0.0.63.9; _qzjto=6.1.0; _qzjb=1.1643039762662.6.0.0.0; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1643040987; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzAyMzZjZDIwZWI0MzFiZDFiMThjNGFkZTAwZTg1ZjEwODAyYjY5ZjEwNjU1N2JhNGMxZDNkM2E1MWE5MzcxNDM0OTgyNTgyMDg1OTZmNzE4N2U1OGZjM2VlYzc4YjIxMTNhYzdhMTBkMWZkMTJlZDUyYjMyOGU4MzZkZTU0MmY4NGIyOTdjZDk0YmM1MWRhOTNmZGIxNTZhOGNiNTgyYTgyMTkwZmUxOGQyNGE4ODg2ODhlNDYwYzM2YWMxZTM5M2NhMGVmOThhYmU0ZTkxY2E3YWY4MmFhOGQ1MDVmOWE1ZTkzMjM5OGNlZDM2N2FhZGFlZGVlNTYzY2ZlOWUyNVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkOTU4ODQwYVwifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL2NoZW5namlhby9tdzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='.encode("utf-8").decode("Latin1"),
    'User-Agent': USER_AGENT
}

property = []
def get_pages():

    regions = ['pudong', 'minhang', 'baoshan', 'xuhui', 'putuo', 'yangpu', 'changning'] #'songjiang', 'jiading', 'huangpu', 'jingan', 'hongkou', 'qingpu', 'fengxian', 'jinshan'
    prices = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
    room_numbers = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6']
    size = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']
    for re in regions:
        for pr in prices:
            for sz in size:
                for rn in room_numbers:
                    while True:
                        try:
                            page = 1
                            url = 'https://sh.lianjia.com/chengjiao/' + re + '/pg' + str(
                                page) + rn + sz + pr + '/'
                            resp = requests.get(url, headers=headers, timeout=6)
                            html = etree.HTML(resp.text)
                            uls = html.xpath("/html/body/div[5]/div[1]/ul")
                            t = (int(html.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/span/text()")[0]) / 30)
                            for dl in uls:
                                title = dl.xpath("./li/div/div[1]/a/text()")
                                price = dl.xpath("./li/div/div[2]/div[3]/span/text()")
                                build_time = dl.xpath("./li/div/div[3]/div[1]/text()")
                                unit_price = dl.xpath("./li/div/div[3]/div[3]/span/text()")
                                transaction_date = dl.xpath("./li/div/div[2]/div[2]/text()")
                                for s in range(len(title)):
                                    property.append(
                                        [title[s], build_time[s], price[s], unit_price[s], transaction_date[s],
                                         re, rn])
                                    csvwriter.writerows(property)
                            if page >= t:
                                break
                            print(
                                "region: " + re + ", price: " + pr + ',size' + sz + 'room_numbers' + rn + ', page: ' + str(
                                    page))
                            page = page + 1
                            time.sleep(2)
                            break

                        except:
                            print("Connection refused by the server..")
                            print("Let me sleep for 5 seconds")
                            print("ZZzzzz...")
                            time.sleep(5)
                            print("Was a nice sleep, now let me continue...")
                            continue




if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=11) as t:
        # t1 = time.time()
        t.submit(get_pages)
        # data = t.submit(strip_blank, 1).result()
        # print(data)
        # t2 = time.time()
        # print(t2 - t1)
