#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015��3��8��
���������һ�����ĸ�λ��ʮλ������
˼�룺��λ:x%10 ʮλ:x/10%10 ��λ:x/100%10 ǧλ:x/1000%10(�ƶ�С����)
@author:ECNU_zenwan
'''
def qushu(a):
    if a in range(0,100):
        print "ʮλ����"+repr(a//10)# //�������߳����κ����������������Ϊ׼
        print "��λ����"+repr(a%10)# 
    else:
        print "Error:����������쳣"
if __name__=='__main__':
    i=input("please enter a int number(0-100):")
    qushu(i)