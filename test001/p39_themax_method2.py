#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��10��
������������(�ǵ���)
if a>b and b>c print"-----"#��ٷ�(6��if)
if b>a and a>c print"-----"#��ٷ�(6��if)
......
@author:ECNU_zenwan
'''
a=input("�����һ����:")
b=input("����ڶ�����:")
c=input("�����������:")
if a>b:
    maxnumber=a;
else:
    maxnumber=b;
if c>maxnumber:
    maxnumber=c  
    print "�������ǣ�"+repr(maxnumber)