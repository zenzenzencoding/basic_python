#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��10��
������������ѭ����䣺1+2+...+99(�ݹ�)
@author:ECNU_zenwan
'''
s=0
def f(start,n):
    if n==start:
        return start
    else: 
        return n+f(start,n-1)
if __name__=='__main__':
    start=input("������ʼֵ��start=")
    end=input("�������ֵ��end=")
    print "result="+repr(f(start,end))