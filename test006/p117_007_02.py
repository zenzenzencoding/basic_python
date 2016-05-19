#-*-coding:utf-8-*-
'''
Created on 2015年4月7日
Description：算法优化
@author:ECNU_zenwan
@version：
'''
lists=[]
s=0
strs=raw_input("输入字符串：").lower()
flag=True
while flag:
    for i in range(-1,-(len(strs)+1),-1):
        if (ord(strs[i]) in range(97,123) and (strs[i] not in lists)):
            lists.append(strs[i])
        if (len(lists)>=10 or i==-len(strs)):
            flag=False 
            break
if len(lists)<10:
    print ("没找到")
else:print lists