#-*-coding:utf-8-*-
'''
Created on 2015��6��9��
Description��p250_003
@author:ECNU_zenwan
@version��
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
print 'Ŀǰ��',zhangsan.display()
zhangsan.deposit(1314)
print '��Ǯ����',zhangsan.display()
zhangsan.withdraw(520)
print 'ȡǮ����',zhangsan.display()

        