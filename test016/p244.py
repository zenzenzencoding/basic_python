#-*-coding:utf-8-*-
'''
Created on 2015��6��16��
Description��
@author:ECNU_zenwan
@version��
'''
from Tkinter import *
root =Tk()
#����˵�������Ӧ�Ļص�����
def openCall():
    print ('�㵥����Openѡ��')
def saveCall():
    print('�㵥����savaѡ��')
def aboutCall():
    print('����Menu�˵��ļ���ʾ')
#�����˵���menubar
menubar=Menu(root)
#���������˵�file,Ȼ������붥���˵���menubar��
filemenu=Menu(menubar)
filemenu.add_command(label='open',command=openCall)
filemenu.add_command(label='save',command=saveCall)
filemenu.add_separator()#�ָ���
filemenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='File',menu=filemenu)#�����˵����ӵ��˵���
#������һ�������˵�help
helpmenu=Menu(menubar)
helpmenu.add_command(label='about',command=aboutCall)
helpmenu.add_command(label='Help',command=helpmenu)
menubar.add_cascade(label='help',menu=helpmenu)#�����˵����ӵ��˵���
#��ʾ�˵�
root.config(menu=menubar)
mainloop()
