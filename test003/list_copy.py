#-*-coding:utf-8-*-
'''
Created on 2015年3月24日
Description：列表copy
@author:ECNU_zenwan
@version：
'''
import copy
l1=[0,1,2,3,4]
l2=copy.copy(l1)#浅拷贝
l3=copy.deepcopy(l1)#深拷贝
l2.append(5)#删除4
l3.append(5)#删除4
print 'l1=',l1
print 'l2=',l2
print 'l3=',l3
