#-*-coding:utf-8-*-
'''
Created on 2015��3��31��
Description���ж�������
@author:ECNU_zenwan
@version��V1.0
'''
a=input("�����1������")
b=input("�����2������")
c=input("�����3������")
d=input("�����4������")
max_number=a#��ʼ�����ֵΪa
if max_number<b:
    max_number=b
if max_number<c:
    max_number=b
if max_number<d:
    max_number=d
print ("�������ǣ�")+repr(max_number)#repr(obj):��obj����ת��Ϊ�ַ���
    