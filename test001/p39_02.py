# -*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
������ŷ������㷨���ݹ飩
˼�룺�����������Լ�����ǳ��������������Լ��
@author:ECNU_zenwan
'''
def gcd(a,b):
    if a<b:
        a,b=b,a #�ȼ���temp=a a=b b=temp
    if (a%b==0):
        return b
    else:
        return gcd(b,a%b)
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    print "���Լ����"+repr(gcd(m,n))

#�ǵݹ�����
# def gcd(a,b):
#     while b:
#         temp=a
#         a=b
#         b=temp%b
#     return b
