#-*-coding:utf-8-*-
'''
Created on 2015年6月16日
Description：
@author:ECNU_zenwan
@version：
'''
from Tkinter import *
root =Tk()
#定义菜单项所对应的回调函数
def openCall():
    print ('你单击了Open选项')
def saveCall():
    print('你单击了sava选项')
def aboutCall():
    print('这是Menu菜单的简单演示')
#创建菜单栏menubar
menubar=Menu(root)
#创建下拉菜单file,然后将其加入顶级菜单栏menubar中
filemenu=Menu(menubar)
filemenu.add_command(label='open',command=openCall)
filemenu.add_command(label='save',command=saveCall)
filemenu.add_separator()#分割线
filemenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='File',menu=filemenu)#下拉菜单增加到菜单栏
#创建另一个下来菜单help
helpmenu=Menu(menubar)
helpmenu.add_command(label='about',command=aboutCall)
helpmenu.add_command(label='Help',command=helpmenu)
menubar.add_cascade(label='help',menu=helpmenu)#下拉菜单增加到菜单栏
#显示菜单
root.config(menu=menubar)
mainloop()
