#-*-coding:utf-8-*-
'''
Created on 2015��4��19��
Description���Ա�
@author:ECNU_zenwan
@version��
'''
a,b,c,s=0,0,0,0
flag=True
n=input("�����������:")
while flag:        
    if a==0:
        if n>=2:
            a=2
            print("A��2����")
            n=n-2
            s=s+2
        elif n<=1:
            a=1
            print("A��1����")
            n=n-1
            s=s+1              
    if b==0:
        if n>=2:
            b=input("BҪ�Լ�����:")
            assert 0<b<=2,"����1��2"
            c=b
            n=n-b
        elif n==1:
            b=1
            c=b
            n=n-1
            print("B����1����")    
    a=a-1
    b=b-1
    if n<=0:
        flag=False
        break
if __name__=="__main__":
    print "Aһ������:%d��"%(s)