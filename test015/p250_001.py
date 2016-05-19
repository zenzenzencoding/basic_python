#-*-coding:utf-8-*-
'''
Created on 2015年6月9日
Description：p250_001
@author:ECNU_zenwan
@version：
'''
#定义Point类
class Point:
    def __init__(self,x1,y1):#初始化点的起始位置
        self.x=x1
        self.y=y1
    def move(self,newX,newY):
        self.x=newX
        self.y=newY
    def show(self):
        print ("现在的位置是(%d,%d)"%(self.x,self.y))
#创建对象测试
p1=Point(2,3)
p1.show()
print("**********移动后**********")
p1.move(5, 6)
p1.show()
