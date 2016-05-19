# -*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月8日
描述：欧几里得算法（递归）
思想：两个数的最大公约数就是除数和余数的最大公约数
@author:ECNU_zenwan
'''
def gcd(a,b):
    if a<b:
        a,b=b,a #等价于temp=a a=b b=temp
    if (a%b==0):
        return b
    else:
        return gcd(b,a%b)
if __name__=='__main__':
    m=input("please enter the first number:")
    n=input("please enter the second number:")
    print "最大公约数是"+repr(gcd(m,n))

#非递归运算
# def gcd(a,b):
#     while b:
#         temp=a
#         a=b
#         b=temp%b
#     return b
