#-*-coding:utf-8-*-
'''
Created on 2015年4月19日
Description：吃饼
@author:ECNU_zenwan
@version：
'''
a,b,c,s=0,0,0,0
flag=True
n=input("输入饼的总数:")
while flag:        
    if a==0:
        if n>=2:
            a=2
            print("A吃2个饼")
            n=n-2
            s=s+2
        elif n<=1:
            a=1
            print("A吃1个饼")
            n=n-1
            s=s+1              
    if b==0:
        if n>=2:
            b=input("B要吃几个饼:")
            assert 0<b<=2,"输入1或2"
            c=b
            n=n-b
        elif n==1:
            b=1
            c=b
            n=n-1
            print("B吃了1个饼")    
    a=a-1
    b=b-1
    if n<=0:
        flag=False
        break
if __name__=="__main__":
    print "A一共吃了:%d个"%(s)