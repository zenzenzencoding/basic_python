#-*-coding:gbk-*-
'''
Created on 2015��6��16��
Description:
@author:ECNU_zenwan
@version��
'''

from Tkinter import *
root=Tk()
root.title('welcome to my GUI')
#����Label ����lab
lab=Label(root,text='welcome to my GUI',width=50,height='10')
#��ʾlab����
lab.pack()

#����ص�����hello()
def hello():
    print ("hello!")
#����ص�����show()
def show():
    inputTxt=entry1.get()
    entry1.delete(0,END)
    entry2.insert(0,inputTxt)
#����Button��ť����btn ͨ��command������ָ��Button�Ļص�����Ϊhello
btn=Button(root,text='button',command=show)
#��ʾbtn����
btn.pack()
#�������ı������entry1
entry1=Entry(root,width=30)
entry1.pack()
#�������ı������entry2
entry2=Entry(root,width=30)
entry2.pack()

cnv=Canvas(root,width=200,height=300)
cnv.pack()
#ʹ��create_line���� ����ֱ��
cnv.create_line(0,0,200,100,width=4)
cnv.create_line(0,100,200,0,fill='red',dash=(4,4))
root.mainloop()


