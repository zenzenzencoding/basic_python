#-*-coding:utf-8-*-
'''
Created on 2015��5��19��
Description��
@author:ECNU_zenwan
@version��
'''
nums=list(open(r'C:\Users\Administrator\Desktop\needsort.txt','r'))
for i in range(0,len(nums)):
        nums[i]=float(nums[i])
nums.sort()
f=open('sorted.txt','w')
for i in range(0,len(nums)):
    f.write(str(nums[i])+'\n')
f.close()
