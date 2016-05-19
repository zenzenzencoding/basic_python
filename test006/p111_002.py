#-*-coding:utf-8-*-
'''
Created on 2015年4月7日
Description：第111页循环结构示例
@author:ECNU_zenwan
@version：1.0
'''
file_a=open("E:\\document\\助教文档\\A.txt",'r')#以写的方式打开文件
file_b=open("E:\\document\\助教文档\\B.txt",'w')#以写的方式打开文件
lists=file_a.readlines()
for line in range(len(lists)):
    element=lists[line].split( )
    result1=float(element[0])+float(element[1])
    result2=float(element[0])-float(element[1])
    result3=float(element[0])*float(element[1])
    result4=float(element[0])/float(element[1])
    file_b.write(element[0]+'+'+element[1]+'='+repr(result1)+'\n')
    file_b.write(element[0]+'-'+element[1]+'='+repr(result2)+'\n')
    file_b.write(element[0]+'*'+element[1]+'='+repr(result3)+'\n')
    file_b.write(element[0]+'/'+element[1]+'='+repr(result4)+'\n')
file_b.close()
file_c=open("E:\\document\\助教文档\\B.txt",'r')
print file_c.readlines()
