#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
������������֧���
@author:ECNU_zenwan
'''
a=input("������һ������")
if a>0 and a-int(a)==0:
    print "��Ч��"
elif a in range(1,100):#Ĭ�ϲ���Ϊ1��ע���1<=a<100������
    print "������"
else:
    print "��Ч��"