#-*-coding:utf-8-*-
'''
Created on 2015��4��28��
Description��p158��2��
@author:ECNU_zenwan
@version��1.0
'''
from datetime import datetime
f1=open(r"E:\document\�����ĵ�\ch5\�ı��ļ�\customer.txt")
now = datetime.now() #��ȡϵͳ��ǰ���ڵ���
gender= dict({1:'��',2:'Ů'})
new_file=[]
#print now.year
while True:
    line=f1.readline()
    if not line:break
    id=line.split()
    years=int(id[1][6:10])#��customer�ĳ������
    mon = int(id[1][10:12])#��customer�ĳ����·�
    da = int(id[1][12:14])#��customer�ĳ�����
    age = now.year- years#ע��ʵ��������㷨��δ�����յĻ���Ҫ��1
    if now.month < mon:
        age -= 1
    elif now.month == mon:
        if now.day < da:
            age -= 1
    if int(id[1][16]) % 2 == 0:#������Ů
        key = 2
    else :
        key = 1
    new_file.append([id[0],gender[key],age])
f2 = open(r"E:\document\�����ĵ�\ch5\�ı��ļ�\cusinfo.txt",'w')
for item in new_file:
    f2.write('%s\t%s\t%d\n'%(item[0],item[1],item[2]))
f1.close()
f2.close()
