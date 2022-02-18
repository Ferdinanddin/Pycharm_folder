import pandas as pd
import numpy as np

import csv
# f = open("链家transaction_information_output(1).csv", mode="w", encoding="utf-8")
# csvwriter = csv.writer(f)
path = "链家transaction_information_output(1).csv"
# 使用pandas读入
data = pd.read_csv(path, encoding='utf-8') #读取文件中所有数据
data.columns = ['title', 'build_time', 'price', 'unit_price', 'transaction_date']
# 按列分离数据
print(data.head())