#-*-coding:utf-8-*-
'''
Created on 2015��5��19��
Description��006
@author:ECNU_zenwan
@version��
'''
f=open(r'C:\Users\Administrator\Desktop\namelist.txt','r')
f2=open(r'C:\Users\Administrator\Desktop\addressofname.txt','w')
while True:
    line=f.readline()
    if not line:
        break
    lines=line.split(',')
    print lines
    if repr(lines[1])=='��':
        f2.write(lines[0]+',����'+'\n')
        print lines[0],lines[1]
    elif repr(lines[1])=='Ů':
        f2.write(lines[0]+',Ůʿ'+'\n')
f.close()
f2.close()
    