#-*-coding:utf-8-*-
'''
Created on 2015年3月24日
Description：求圆柱体积
@author:ECNU_zenwan
@version：V2.79
'''
import math
radius=int(input("输入半径："))
height=int(input("输入高度"))
volumn=math.pi*math.pow(radius,2)*height
print '体积=', volumn
