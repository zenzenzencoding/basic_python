#-*-coding:utf-8-*-
'''
Created on 2015年4月29日
Description：p159_04
@author:ECNU_zenwan
@version：
'''
f3 = open(r"E:\document\助教文档\ch5\文本文件\hamlet.txt")
c = f3.read()
print(c)
v1 = raw_input('动作1:')
v2 = raw_input('动作2:')
adj =raw_input('形容词:')
n = raw_input('名词:')
c=c.replace('<verb1>',v1)
c=c.replace('<verb2>',v2)
c=c.replace('<adjective>',adj)
c=c.replace('<noun>',n)
print(c)