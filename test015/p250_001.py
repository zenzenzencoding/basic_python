#-*-coding:utf-8-*-
'''
Created on 2015��6��9��
Description��p250_001
@author:ECNU_zenwan
@version��
'''
#����Point��
class Point:
    def __init__(self,x1,y1):#��ʼ�������ʼλ��
        self.x=x1
        self.y=y1
    def move(self,newX,newY):
        self.x=newX
        self.y=newY
    def show(self):
        print ("���ڵ�λ����(%d,%d)"%(self.x,self.y))
#�����������
p1=Point(2,3)
p1.show()
print("**********�ƶ���**********")
p1.move(5, 6)
p1.show()
