#-*-coding:utf-8-*-
'''
Created on 2015年4月29日
Description：p159_第5题
@author:ECNU_zenwan
@version：
'''
filename=raw_input("input file:")
L=list(open(filename))
n=int(L[0])
lines=[]
p=[]
s=""       
for i in range(1,len(L)):
    if(i<=n):
        lines.append(L[i].split(":"))
        p.append(raw_input(lines[i-1][1]))
    else:
        s+=L[i]
      
print(lines)
print(p)
print(s)
for i in range(0,n):
    s=s.replace(lines[i][0],p[i])
print(s)