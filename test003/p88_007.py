#-*-coding:utf-8-*-
'''
Created on 2015��3��21��
Description�����
@author:ECNU_zenwan
@version��
'''
listdic={10:'A',9:'A',8:'B',7:'C',6:'D',5:'E',4:'E',3:'E',2:'E',1:'E',0:'E'}
def dengjihanshu(n):
    dengji=n//10
    return listdic[dengji]
x=input("����ɼ�:")#2.7�汾���ܵ������ֲ����ַ���������Ҫ����ת��
print ("�ɼ��Ǽ���"+dengjihanshu(x))
