#-*-coding:utf-8-*-
'''
Created on 2015��4��7��
Description��������
@author:ECNU_zenwan
@version��
'''
lists=[]
s=0
string1=raw_input("�����ַ�����")
strs=string1[::-1]
for i in range(len(strs)):
    if (ord(strs[i]) in range(97,123) or ord(strs[i])in range(65,91)) and (strs[i] not in lists):
        lists.append(strs[i])
if len(lists)<10:print "û�ҵ�"
else:print lists[0:10]
        
