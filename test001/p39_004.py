#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
���������Լ��(���������)
˼�룺�����������Լ�����ǳ��������������Լ��
@author:ECNU_zenwan
'''
def gxjss(a,b):
    if a<b:
        a,b=b,a #�ȼ���temp=a a=b b=temp
    if (a==b):
        return b
    else:
        return gxjss(b,a-b)
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    print "���Լ����"+repr(gxjss(m,n))
    