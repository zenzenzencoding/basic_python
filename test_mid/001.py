#-*-coding:utf-8-*-
'''
Created on 2015年5月12日
Description：期中考试第1题
@author:ECNU_zenwan
@version：1.0
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
        print ("完数：%d,因子包括："%a),#一个逗号，不换行输出
        print(L1)


       
