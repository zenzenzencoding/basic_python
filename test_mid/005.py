#-*-coding:utf-8-*-
'''
Created on 2015��5��12��
Description����̴�ӡ�����Ǻţ�����ʹ��ѭ�����
@author:ECNU_zenwan
@version��
'''
n=input("����n:")
i=0
for i in range(n):
    j=i
    if i<=(n/2):
        print ' '*((n-(i*2+1))/2),
        print '*'*(2*i+1)
    else:
        i=n-i
        print ' '*((n-(i*2+1))/2),
        print '*'*(2*i+1)
    
    
        