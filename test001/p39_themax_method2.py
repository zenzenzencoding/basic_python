#-*-coding: utf-8-*-
#!/usr/bin/python
'''
Created on 2015年3月10日
描述：最大的数(非迭代)
if a>b and b>c print"-----"#穷举法(6个if)
if b>a and a>c print"-----"#穷举法(6个if)
......
@author:ECNU_zenwan
'''
a=input("输入第一个数:")
b=input("输入第二个数:")
c=input("输入第三个数:")
if a>b:
    maxnumber=a;
else:
    maxnumber=b;
if c>maxnumber:
    maxnumber=c  
    print "最大的数是："+repr(maxnumber)