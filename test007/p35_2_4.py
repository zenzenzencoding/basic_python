#-*-coding:utf-8-*-
'''
Created on 2015��4��14��
Description��4
@author:ECNU_zenwan
@version��
'''  
def f(n):
    if n==1:return 1
    if n==2:return 1
    if n==3:return 2
    else:
        return f(n-1)+f(n-3)
print f(30)
 
   
 
        
        