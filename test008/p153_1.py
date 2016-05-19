#-*-coding:utf-8-*-
'''
Created on 2015年4月21日
Description：第153页第一题
@author:ECNU_zenwan
@version：1.0
'''
l=input("Input L(litre):")
sc=l*90
water=l*1000-sc
print "sodium chloride:%.1f ml\nWater:%.1f ml"%(sc,water)
