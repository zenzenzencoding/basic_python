#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��10��
����������������������(����)
@author:ECNU_zenwan
'''
def maxnumber(a,b):
    if a>b:
        return a
    else:
        return b
if __name__=='__main__':
    x=input("�����һ������")
    y=input("����ڶ�������")
    z=input("�������������")
    return maxnumber(x, maxnumber(y, z))