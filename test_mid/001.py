#-*-coding:utf-8-*-
'''
Created on 2015��5��12��
Description�����п��Ե�1��
@author:ECNU_zenwan
@version��1.0
'''
m=10
for a in range(2,m+1):
    s=a
    L1=[]
    for i in range(1,a):
        if a%i==0:
            s-=i
            L1.append(i)
    if s==0:
        print ("������%d,���Ӱ�����"%a),#һ�����ţ����������
        print(L1)


       
