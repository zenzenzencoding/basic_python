#-*-coding:utf-8-*-
'''
Created on 2015��5��26��
Description��
@author:ECNU_zenwan
@version��
'''
m=input("m=")
s=0
def jiecheng(n):
    if n==1:
        return 1
    else:
        return jiecheng(n-1)*n
for i in range(m,0,-1):
    s+=jiecheng(i)  
print s
       


    
