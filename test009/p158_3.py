#-*-coding:utf-8-*-
'''
Created on 2015��4��28��
Description����3��
@author:ECNU_zenwan
@version��
'''
import os
sour_dir = raw_input('����Դ�ļ���:')
dest_dir = raw_input('����Ŀ���ļ���:')
if not os.path.exists(sour_dir):
    print('Դ�ļ�������')
else: #Դ�ļ�����
    isnot = ''
    if os.path.exists(dest_dir):
        isnot = input('Ŀ���ļ��Ѿ����ڣ��Ƿ񸲸Ǹ��ļ�?(y/n):')
    if isnot == 'n':
        print('ȡ������')
    if not os.path.exists(dest_dir) or isnot == 'y':
        f3 = open(sour_dir)
        a = f3.read()
        f4 = open(dest_dir,'w')
        f4.write(a)
        #f4.seek(0)
        f4.close()
        print('�ļ����Ƴɹ�!')