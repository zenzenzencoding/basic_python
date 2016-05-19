 #-*-coding:utf-8-*-
'''
Created on 2015Äê6ÔÂ9ÈÕ
Description£º004
@author:ECNU_zenwan
@version£º
'''
__metaclass__=type
class Employee:
    def __init__(self,name,position,gender,salary):
        self.name=name
        self.position=position
        self.gender=gender
        self.salary=salary
    def showInfo(self):
        print self.name
        print self.gender
        print self.position
        print self.salary
    
class  jingli(Employee):
    def __init__(self,name,position,gender,salary,salary1=8000):
        super(jingli, self).__init__(name,position,gender,salary)
        self.salsry1=salary1
    def getSalary(self):
        return self.salary+self.salsry1
class  jishu(Employee):
    def __init__(self,name,position,gender,salary,time=40):
        super(jishu, self).__init__(name,position,gender,salary)
        self.time=time
    def getSalary(self):
        return self.salary+self.time*30
class  xiaoshou(Employee):
    def __init__(self,name,position,gender,salary,num=100000):
        super(xiaoshou, self).__init__(name,position,gender,salary) 
        self.num=num
    def getSalary(self):
        return self.salary+self.num*0.05
jing=jingli('jingli','jinglier','man',1000,8000)
jing.showInfo()
print jing.getSalary()
jishu=jishu('jishu','jishuer','man',1000,40)
jishu.showInfo()
print jishu.getSalary()
xiaoshou=xiaoshou('xiaoshou','xiaoshou','woman',1000)
xiaoshou.showInfo()
print xiaoshou.getSalary()
