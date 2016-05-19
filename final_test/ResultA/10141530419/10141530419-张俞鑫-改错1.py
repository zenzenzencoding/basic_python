Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:55:48) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> help(when)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    help(when)
NameError: name 'when' is not defined
>>> help(del)
SyntaxError: invalid syntax
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(while)
SyntaxError: invalid syntax
>>> import math
>>> math.floor(5.5)
5
>>> math.floor(5.678)
5
>>> help(math.floor)
Help on built-in function floor in module math:

floor(...)
    floor(x)
    
    Return the floor of x as an int.
    This is the largest integral value <= x.

>>> math.floor(-5.678)
-6
>>> print('welcome/neverybody')
welcome/neverybody
>>> print('welcome'/n'everybody'),
SyntaxError: invalid syntax
>>> print('welcome'+/n'everybody')
SyntaxError: invalid syntax
>>> print('welcome'/n'everybody')
SyntaxError: invalid syntax
>>> print('welcome\neverybody')
welcome
everybody
>>> s1={1,2,3}
>>> s2={2,3,4}
>>> s1|s2
{1, 2, 3, 4}
>>> len(s1|s2)
4
>>> ================================ RESTART ================================
>>> 
请输入一个正整数：12
转换为二进制的数据为： 
>>> ================================ RESTART ================================
>>> 
请输入一个正整数：12\
Traceback (most recent call last):
  File "C:\ECNU_KS\root\bug1.py", line 8, in <module>
    x=int(input('请输入一个正整数：'))
ValueError: invalid literal for int() with base 10: '12\\'
>>> ================================ RESTART ================================
>>> 
请输入一个正整数：12
转换为二进制的数据为：
>>> ================================ RESTART ================================
>>> 
请输入一个正整数：12
转换为二进制的数据为： 1100
>>> ================================ RESTART ================================
>>> 
请输入一个正整数：10
转换为二进制的数据为： 1010
>>> 
