#-*-coding:utf-8-*-
'''
Created on 2015Äê4ÔÂ14ÈÕ
Description£º4
@author:ECNU_zenwan
@version£º
'''  
def f(n):
    if n==1:return 1
    if n==2:return 1
    if n==3:return 2
    else:
        return f(n-1)+f(n-3)
print f(30)
 
   
 
        
        