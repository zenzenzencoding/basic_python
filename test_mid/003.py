#-*-coding:utf-8-*-
'''
Created on 2015��5��12��
Description������һ���ַ����ֱ�ͳ�Ƴ�����Ӣ����ĸ���ո����ֺ������ַ��ĸ�����
@author:ECNU_zenwan
@version��
'''
letter,space,digit,other=0,0,0,0
s =raw_input('input a string:')
for c in s:
    if 'a'<=c.lower()<='z':
        letter +=1
    elif c.isspace():
        space +=1
    elif c.isdigit():
        digit +=1
    else:
        other+=1
print("��ĸ����%d\n�ո�����%d\n��������%d\n�����ַ�����%d\n"%(letter,space,digit,other))
