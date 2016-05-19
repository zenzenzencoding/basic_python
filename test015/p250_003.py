#-*-coding:utf-8-*-
'''
Created on 2015年6月9日
Description：p250_003
@author:ECNU_zenwan
@version：
'''
class Acount:
    def __init__(self,id,balance=0):
        self.ID=id
        self.Balance=balance
    def deposit(self,c_num):
        self.Balance+=c_num
        return self.Balance
    def withdraw(self,q_num):
        self.Balance-=q_num
    def display(self):
        return self.Balance
zhangsan=Acount('5201314')
print '目前余额：',zhangsan.display()
zhangsan.deposit(1314)
print '存钱后余额：',zhangsan.display()
zhangsan.withdraw(520)
print '取钱后余额：',zhangsan.display()

        