import pandas as pd
import numpy as np
import csv
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def np导入CSV():  # 思路就是用一个dic来存储csv中的参数和值，值用列表存储
    all_pmu_dic = {}
    with open(path, encoding="utf-8") as f:
        item = np.loadtxt(path, dtype=str, delimiter=',', )
        data = np.loadtxt(path, delimiter=',', skiprows=1)
        for i in range(len(item[0])):
            all_pmu_dic[str(item[0][i])] = {'key名': data[1:, i]}


def strip_blank():  ###清洗数据第一步，清理空白行
    with open('lianjia_without_blank(1).csv', 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(df):
            if any(field.strip() for field in row):
                writer.writerow(row)



def duplicated():  # 检查有无重复数据，把每列都写上
    df = pd.read_csv('test_file_cleaned.csv', encoding='utf-8')
    df.columns= ['0','title', 'build_time', 'unit_price', 'transaction_date']
    df.drop_duplicates(subset = ['title', 'build_time', 'unit_price', 'transaction_date'], keep='first', inplace=True)
    df.to_csv('test_file_cleaned(modified).csv', encoding='utf-8')


def split_colume():  # 将csv文件用pandas读出， 然后将其中某列根据特征分开，变成分开的series，然后重新写入字典，饭后用dataframe处理，写入新的CSV
    # 既保证了数据的完整性，又完成了分割
    # path = 'd:/桌面/同步文件夹/Pycharm folder/lianjia2.csv'
    # 使用pandas读入
    data = pd.read_csv(path)  # 读取文件中所有数据
    data.columns = ['title', 'build_time', 'price', 'unit_price', 'transaction_date']
    fst = data['title']
    sed = data['build_time']
    adress = fst.str.split(" ", expand=True)
    adress.columns = ['title', 'rest','c','d']
    age = sed.str.split(" ", expand=True)
    age.columns = ['height', 'year']
    s1 = adress['title']
    s2 = age['year']
    s5 = data['price']
    s6 = data['unit_price']
    s7 = data['transaction_date']
    lst = {s1.name: s1, s2.name: s2,  s6.name: s6, s7.name: s7}
    datas = pd.DataFrame(lst)
    datas.to_csv('d:/桌面/同步文件夹/Pycharm folder/test_file_cleaned.csv', header=True)

def drop():
    Data[~Data['c'].isin(['年'])]
    df_clear = df.drop(df[df['x'] < 0.01].index)


def split_file():
    # 分割后的子文件存储路径
    workspace = 'E:/testFile/workspace'

    with open(path, 'r', newline='', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        a = next(csvreader)
        # print(a)
        i = j = 0
        for row in csvreader:
            print(row)
            # 每 500000 个就 j 加 1，然后就有一个新的文件名。 大约46MB一个文件
            if i % 10000000 == 0:
                j += 1

            csv_path = os.path.join(workspace, 'part_{}.csv'.format(j))

            print(csv_path)
            # 不存在此文件的时候，就创建
            if not os.path.exists(os.path.dirname(csv_path)):
                os.makedirs(os.path.dirname(csv_path))
                with open(csv_path, 'w', newline='', encoding='utf-8') as file:

                    csvwriter = csv.writer(file)
                    # 表头为啥老是加不上呢 ？？？
                    # csvwriter.writerow(['账务流水号', '业务流水号', '商户订单号', '商品名称', '发生时间', '对方账号', '收入金额（+元）'
                    # , '支出金额（-元）', '账户余额（元）', '交易渠道', '业务类型', '备注'])
                    csvwriter.writerow(row)
                i += 1
            # 存在的时候就往里面添加
            else:
                with open(csv_path, 'a', newline='', encoding='utf-8') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(row)
                i += 1

def merge():
    '''
    Data:2017-07-13
    Auther;JXNU Kerwin
    Description:使用Pandas拼接多个CSV文件到一个文件（即合并）
    '''
    import pandas as pd
    import os
    Folder_Path = r'C:\foldername'  # 要拼接的文件夹及其完整路径，注意不要包含中文
    SaveFile_Path = r'C:\foldername'  # 拼接后要保存的文件路径
    SaveFile_Name = r'all.csv'  # 合并后要保存的文件名

    # 修改当前工作目录
    os.chdir(Folder_Path)
    # 将该文件夹下的所有文件名存入一个列表
    file_list = os.listdir()

    # 读取第一个CSV文件并包含表头
    df = pd.read_csv(Folder_Path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改

    # 将读取的第一个CSV文件写入合并后的文件保存
    df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False)

    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1, len(file_list)):
        df = pd.read_csv(Folder_Path + '\\' + file_list[i])
        df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')
'''
如果要进行多条件筛选，并且这些条件之间是“逻辑与”的关系，可以用“&”符号连接多个筛选条件。

需要注意的是，每个条件要分别用括号括起来。

>>> c = data[(data['产品'] == '单肩包') & (data['数量(个)'] > 60)]
>>> print(c)
     编号   产品  成本价(元/个)  销售价(元/个)  数量(个)  成本(元)  收入(元)  利润(元)
5  a006  单肩包        58       124     63   3654   7812   4158


'''
if __name__ == '__main__':

    duplicated()
    # path = 'test_file.csv'
    # split_colume()
    # with open(path, encoding='utf-8') as df:
    #     df.columns = ['title', 'build_time', 'price', 'unit_price', 'transaction_date','district', 'bedrooms']
    #
    #     strip_blank()

    #     with ThreadPoolExecutor(max_workers=5) as t:
    #         t1 = time.time()
    #         t.submit(strip_blank, 1)
    #         data = t.submit(strip_blank, 1).result()
    #         print(data)
    #         t2 = time.time()
    #         print(t2 - t1)
            # obj_list = []
            # begin = time.time()
            # for page in range(1, 15):
            #     obj = t.submit(spider, page)
            #     obj_list.append(obj)
            #
            # for future in as_completed(obj_list):
            #     data = future.result()
            #     print(data)
            #     print('*' * 50)
            # times = time.time() - begin
            # print(times)

        # t1 = time.time()
        # strip_blank(1)
        # t2 = time.time()
        # print(t2 - t1)


    #
    # np导入CSV()


    # split_file()




