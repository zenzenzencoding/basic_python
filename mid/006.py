#-*-coding:utf-8-*-
'''
Created on 2015年5月19日
Description：006
@author:ECNU_zenwan
@version：
'''
f=open(r'C:\Users\Administrator\Desktop\namelist.txt','r')
f2=open(r'C:\Users\Administrator\Desktop\addressofname.txt','w')
while True:
    line=f.readline()
    if not line:
        break
    lines=line.split(',')
    print lines
    if repr(lines[1])=='男':
        f2.write(lines[0]+',先生'+'\n')
        print lines[0],lines[1]
    elif repr(lines[1])=='女':
        f2.write(lines[0]+',女士'+'\n')
f.close()
f2.close()
    