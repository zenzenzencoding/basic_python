#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
�˽��±����ĸ���
@author:ECNU_zenwan
'''
def bl(a,b):
    print "a��ַ��"+repr(id(a))
    print "b��ַ��"+repr(id(b))
    if a<b:
        a,b=b,a #����a��
    print "����:"+repr(a)
    print "С��:"+repr(b)
    print "a�µ�ַ��"+repr(id(a))
    print "b�µ�ַ��"+repr(id(b))
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    bl(m, n)