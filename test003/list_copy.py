#-*-coding:utf-8-*-
'''
Created on 2015��3��24��
Description���б�copy
@author:ECNU_zenwan
@version��
'''
import copy
l1=[0,1,2,3,4]
l2=copy.copy(l1)#ǳ����
l3=copy.deepcopy(l1)#���
l2.append(5)#ɾ��4
l3.append(5)#ɾ��4
print 'l1=',l1
print 'l2=',l2
print 'l3=',l3
