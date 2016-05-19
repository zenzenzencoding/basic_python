#-*-coding:utf-8-*-
'''
Created on 2015年4月7日
Description：判断是否全为英文字母 chr(65)=='A' ord('A')==65
@author:ECNU_zenwan
@version：
'''
strs=raw_input("输入字符串:")
'''
while strs.isalpha():
    print ("都是字母")    
else:
    print ("不全是英文字母")
'''
s=0
for i in range(len(strs)):
    if ord(strs[i]) in range(97,123) or ord(strs[i])in range(65,91):
        s=s+1;
if s==len(strs):
    print ("全是字母")
else:
    print("不都是字母")

        
    