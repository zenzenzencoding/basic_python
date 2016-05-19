#-*-coding:utf-8-*-
'''
Created on 2015年5月12日
Description：输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数。
@author:ECNU_zenwan
@version：
'''
letter,space,digit,other=0,0,0,0
s =raw_input('input a string:')
for c in s:
    if 'a'<=c.lower()<='z':
        letter +=1
    elif c.isspace():
        space +=1
    elif c.isdigit():
        digit +=1
    else:
        other+=1
print("字母数：%d\n空格数：%d\n数字数：%d\n其他字符数：%d\n"%(letter,space,digit,other))
