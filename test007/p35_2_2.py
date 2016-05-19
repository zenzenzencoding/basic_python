#-*-coding:utf-8-*-
'''
Created on 2015年4月14日
Description：p35 2-2
@author:ECNU_zenwan
@version：求解灯谜
'''
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            s1=100*a+10*b+c
            s2=10*c+b
            s3=10*c+a
            if s1-s2==s3:
                print ('a:%d\nb:%d\nc:%d\n')%(a,b,c)

