#-*-coding:utf-8-*-
'''
Created on 2015年4月14日
Description：5 贪心算法
@author:ECNU_zenwan
@version：
'''
def eat(n,a=0,c=0):
    result=0
    n=int(n)
    if a==0:
        if(n<=2):
            print('a take ',n)
            a=n
            return n
        else:
            print('a take ',2)
            a=2
            result+=2
            n-=2
    if c==0:
        b=input('Please input b take:\n')
        b=int(b)
        c=b
    a=a-1
    c=c-1
    if(n-b<=0):
        return result
    else:
        return result+eat(n-b,a,c)
n=input('Please input your n:\n')
print('a total:',eat(n))


    

