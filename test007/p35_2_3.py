#-*-coding:utf-8-*-
'''
Created on 2015Äê4ÔÂ14ÈÕ
Description:p35_2_3
@author:ECNU_zenwan
@version:v1.0
'''
result=[]
for x in range(0,5):
    for y in range(0,4):
        s=0.3*x+0.5*y
        if s!=0:
            result.append(round(s,1))
            s=set(result)
print s
        