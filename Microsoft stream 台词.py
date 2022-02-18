# -*- encoding:utf-8 -*-
from lxml import etree
import codecs


f=codecs.open("Echo360.html","r","utf-8")
content=f.read()
f.close()
html=etree.HTML(content)

node_list =html.xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div[4]/div[2]/div/p/span/text()')

w = open('transcripts_2022_01_31.txt','w')
# w.writelines(node_list)
# w.close()
for i in range(len(node_list)):
    w.write(node_list[i] + '\n')
w.close()
print('finish')






