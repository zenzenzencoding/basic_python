#-*-coding:utf-8-*-
'''
Created on 2015年5月19日
Description：
@author:ECNU_zenwan
@version：
'''
sn=100
hn=float(sn/2)
for n in range(2,11):
    sn=sn+hn*2
    hn=hn/2
print("第10次落地经过%.2f米\n第10次反弹高度为%.2f米。")%(sn,hn)