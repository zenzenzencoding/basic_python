#-*-coding:utf-8-*-
'''
Created on 2015��3��24��
Description��88ҳ��4��
@author:ECNU_zenwan
@version��
'''
s1=[0,1,2,3,4,5,6]
s2=['SUN','MON','TUE','WED','THU','FRI','SAT']
s5=[]
print ('|'.join(s2))
print (s1[3:5]*3)
for i in range(0,6,1):
    s5.append([s1[i],s2[i]])
print s5