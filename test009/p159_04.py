#-*-coding:utf-8-*-
'''
Created on 2015��4��29��
Description��p159_04
@author:ECNU_zenwan
@version��
'''
f3 = open(r"E:\document\�����ĵ�\ch5\�ı��ļ�\hamlet.txt")
c = f3.read()
print(c)
v1 = raw_input('����1:')
v2 = raw_input('����2:')
adj =raw_input('���ݴ�:')
n = raw_input('����:')
c=c.replace('<verb1>',v1)
c=c.replace('<verb2>',v2)
c=c.replace('<adjective>',adj)
c=c.replace('<noun>',n)
print(c)