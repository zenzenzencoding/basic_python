#-*-coding:utf-8-*-
'''
Created on 2015��6��9��
Description��002
@author:ECNU_zenwan
@version��
'''
#����Car��
class Car:
    def __init__(self,num,speed=0):
        self.id=num
        self.speed=speed
    #����getID����������ȡ���ƺ�
    def getID(self):
        return self.id
    #����getSpeed()������ȡ����
    def getSpeed(self):
        return self.speed
    #change car speed
    def changeCarSpeed(self,newSpeed):
        self.speed=newSpeed
    def stop(self):
        self.speed=0
# creat objection
print('******Car1********')
car1=Car('��A520')
print("���ƺ�"+car1.getID()+"��ʼ����Ϊ��"+repr(car1.getSpeed()))
car1.changeCarSpeed(80)
print("���ƺ�"+car1.getID()+"Ŀǰ����Ϊ��"+repr(car1.getSpeed()))
car1.stop()
print("���ƺ�"+car1.getID()+"ͣ������Ϊ��"+repr(car1.getSpeed()))
print('******Car2********')
car2=Car('��A1314',520)
print("���ƺ�"+car2.getID()+'��ʼ����Ϊ'+repr(car2.getSpeed()))


        