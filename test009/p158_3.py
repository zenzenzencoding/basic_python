#-*-coding:utf-8-*-
'''
Created on 2015年4月28日
Description：第3题
@author:ECNU_zenwan
@version：
'''
import os
sour_dir = raw_input('输入源文件名:')
dest_dir = raw_input('输入目标文件名:')
if not os.path.exists(sour_dir):
    print('源文件不存在')
else: #源文件存在
    isnot = ''
    if os.path.exists(dest_dir):
        isnot = input('目标文件已经存在，是否覆盖该文件?(y/n):')
    if isnot == 'n':
        print('取消复制')
    if not os.path.exists(dest_dir) or isnot == 'y':
        f3 = open(sour_dir)
        a = f3.read()
        f4 = open(dest_dir,'w')
        f4.write(a)
        #f4.seek(0)
        f4.close()
        print('文件复制成功!')