#-*-coding:utf-8-*-
'''
Created on 2015年4月7日
Description：第七题
@author:ECNU_zenwan
@version：
'''
lists=[]
s=0
string1=raw_input("输入字符串：")
strs=string1[::-1]
for i in range(len(strs)):
    if (ord(strs[i]) in range(97,123) or ord(strs[i])in range(65,91)) and (strs[i] not in lists):
        lists.append(strs[i])
if len(lists)<10:print "没找到"
else:print lists[0:10]
        
