#-*-coding:utf-8-*-
'''
Created on 2015��4��7��
Description���ж��Ƿ�ȫΪӢ����ĸ chr(65)=='A' ord('A')==65
@author:ECNU_zenwan
@version��
'''
strs=raw_input("�����ַ���:")
'''
while strs.isalpha():
    print ("������ĸ")    
else:
    print ("��ȫ��Ӣ����ĸ")
'''
s=0
for i in range(len(strs)):
    if ord(strs[i]) in range(97,123) or ord(strs[i])in range(65,91):
        s=s+1;
if s==len(strs):
    print ("ȫ����ĸ")
else:
    print("��������ĸ")

        
    