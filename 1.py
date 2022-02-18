import pandas as pd
import csv
import os
from functools import reduce

# df1 = pd.read_csv('merge_data_modified(3.0).csv', encoding='utf-8')
# # print(df.head())
# # df['位置'] = pd.to_datetime(df['transaction_date'])
# # print(df.head())
#
# df2 = pd.read_csv('处理后经纬度.csv', encoding ='utf-8')
# df = [df1,df2]
# df_merge= reduce(lambda left,right: pd.merge(left,right,on=['title','title']), df)
#
# # df = df1.append(df2, ignore_index=True)
# print(df_merge)
# # df = df['位置'].fillna(value='Non', inplace=True)
# # df = df['经纬度'].fillna(value='Non', inplace=True)
#
# # df4 = df3[df3['位置'].str.contains('上海')]
# # df4.to_csv('cleaned_data(1.0).csv', encoding='utf-8', index=False)
# # print(df4.shape)
# # print( df1.sort_values(by=['transaction_date'], ascending=1))
# # datas = pd.DataFrame(lst)
# df_merge.to_csv('cleaned_data(1.0).csv', header=True, index=False)

df = pd.read_csv('cleaned_data(1.0).csv', encoding='utf-8')
# df.columns = ['title', 'build_time', 'price', 'unit_price', 'transaction_date', 'district', 'bedrooms']
df.drop_duplicates(keep='first', inplace=True)  # 保留第一个重复值
df.to_csv('cleaned_data(2.0).csv', encoding='utf-8',index=False)