#-*-coding:utf-8-*-
'''
Created on 2015��4��21��
Description:p153_3
@author:ECNU_zenwan
@version:V1.0
'''
t=[]
flag=True
while flag:
    num=input("�����¶ȣ�")
    if num!='end':
        t.append(num)
    else:
        flag=False
        break
a,b,c,t_sum=0,0,0,0
for item in t:
    t_sum+=item
    if item>=85:a+=1
    if 85>item>=60:b+=1
    if item<60:c+=1
avg=round(float(t_sum)/len(t),1)
print("��������:%d\n��������:%d\n��������:%d\nƽ������:%.1f")%(a,b,c,avg)
    
    