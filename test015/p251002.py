#-*-coding:utf-8-*-
'''
Created on 2015年6月9日
Description：002
@author:ECNU_zenwan
@version：
'''
#定义Car类
class Car:
    def __init__(self,num,speed=0):
        self.id=num
        self.speed=speed
    #定义getID（）方法获取车牌号
    def getID(self):
        return self.id
    #定义getSpeed()方法获取车速
    def getSpeed(self):
        return self.speed
    #change car speed
    def changeCarSpeed(self,newSpeed):
        self.speed=newSpeed
    def stop(self):
        self.speed=0
# creat objection
print('******Car1********')
car1=Car('沪A520')
print("车牌号"+car1.getID()+"起始车速为："+repr(car1.getSpeed()))
car1.changeCarSpeed(80)
print("车牌号"+car1.getID()+"目前车速为："+repr(car1.getSpeed()))
car1.stop()
print("车牌号"+car1.getID()+"停车后车速为："+repr(car1.getSpeed()))
print('******Car2********')
car2=Car('沪A1314',520)
print("车牌号"+car2.getID()+'起始车速为'+repr(car2.getSpeed()))


        