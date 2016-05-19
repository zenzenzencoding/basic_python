#-*-coding:gbk-*-
'''
Created on 2015年6月16日
Description:
@author:ECNU_zenwan
@version：
'''

from Tkinter import *
root=Tk()
root.title('welcome to my GUI')
#创建Label 对象lab
lab=Label(root,text='welcome to my GUI',width=50,height='10')
#显示lab对象
lab.pack()

#定义回调函数hello()
def hello():
    print ("hello!")
#定义回调函数show()
def show():
    inputTxt=entry1.get()
    entry1.delete(0,END)
    entry2.insert(0,inputTxt)
#创建Button按钮对象btn 通过command属性来指定Button的回调函数为hello
btn=Button(root,text='button',command=show)
#显示btn对象
btn.pack()
#创建上文本框对象entry1
entry1=Entry(root,width=30)
entry1.pack()
#创建下文本框对象entry2
entry2=Entry(root,width=30)
entry2.pack()

cnv=Canvas(root,width=200,height=300)
cnv.pack()
#使用create_line方法 绘制直线
cnv.create_line(0,0,200,100,width=4)
cnv.create_line(0,100,200,0,fill='red',dash=(4,4))
root.mainloop()


