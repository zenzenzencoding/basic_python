#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
������ѭ����䣺1+2+...+99(�ǵݹ�)
@author:ECNU_zenwan
'''
def mysum(a,b):
    s=0
    for i in range(a,b+1):
        s=s+i
    return s   
if __name__=='__main__':
    x=input("��������ʼ����")
    y=input("�������������")
    print "��͵ã�"+repr(mysum(x,y))