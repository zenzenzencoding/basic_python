#-*-coding:utf-8-*-
'''
Created on 2015��3��17��
description���ַ�������
@author:ECNU_zenwan
@version��1.0
'''
import string
s1='programming'
s2='language'
print s1[0:-4]#program
print string.capitalize(s1[0:3])+string.capitalize(s2[0:3])#ProLan
print s1[0:4].capitalize()+s2[0:4].capitalize()#ProLan
print (s1[5:7]+' ')*3
print ' '.join([s1,s2])#join��ʹ�ã��Կո����������е��ַ���
print s1[0:5]+'@'+s1[5:]+' '+s2.replace('l', 'l@').replace('u','u@')