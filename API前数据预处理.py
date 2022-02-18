import csv
import pandas as pd
import shutil

# f = open("adress.csv", mode="w", encoding="utf-8")
# csvwriter = csv.writer(f)
path = 'd:/桌面/同步文件夹/Pycharm folder/lianjia2.csv'
# 使用pandas读入
data = pd.read_csv(path) #读取文件中所有数据
data.columns = ['title', 'build_time', 'price', 'unit_price', 'transaction_date']
# 按列分离数据
# print(data.head())
# x = data[['ImageID', 'label']]#读取某两列
# row = []
fst = data['title']
adress = fst.str.split(" ", expand=True)
adress.columns = ['title', 'No_beadrooms','size', 'none']
s1 =adress['title']
s2 = adress['No_beadrooms']
s3 = adress['size']
s4 = data['build_time']
s5 = data['price']
s6 = data['unit_price']
s7 = data['transaction_date']

# # for row in fst:#读取某一列
# #     fst.sp
# # for i in adress[0]:
# #     row.append(i).str
lst = {s1.name:s1,s2.name:s2, s3.name:s3,s4.name:s4,s5.name:s5,s6.name:s6,s7.name:s7 }
datas = pd.DataFrame(lst)
datas.to_csv('d:/桌面/同步文件夹/Pycharm folder/adress.csv', header=True)
# lst.to_csv(path,mode = 'a',index =False)

# csvwriter.writerows(adress[0])
print("转换完成")



# data=pd.read_csv(path,encoding='utf-8',sep=None,delimiter=",",error_bad_lines=False)
# columns=data.columns.tolist()   ##获取字段
# ##判断字段是否需要拆分
# split_col=[]  ##记录需要拆分的字段
# for i in columns:
#     num=0
#     #print(i)
#     #print(data[i])
#     temp=data[i].dropna()  ##去掉字段中的空值
#     #print(len(data[i]),len(temp))
#     if len(temp)>0:  ##对于有取值的字段，判断是否需要进行拆分
#         for j in temp:
#             if ":" in str(j) and "http:" not in str(j) and "https:" not in str(j):
#                num+=1
#         if num==len(temp):
#             #print("需拆分:",i)
#             split_col.append(i)
# print("需要拆分的字段：",split_col)


# frame=pd.read_csv('D:\Desktop\transaction_data(PG2-100)(fangtianxia).csv',engine='python')
# data = frame.drop_duplicates(subset=['id'], keep='first', inplace=False)
# data.to_csv('path+name', encoding='utf8')
