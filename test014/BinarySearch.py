#-*-coding:utf-8-*-
'''
Created on 2015��6��2��
Description���۰���ң��ݹ�ͷǵݹ飩
@author:ECNU_zenwan
@version��
'''

#�ǵݹ�
def binarysearch(listorder,num):
    left=0
    right=len(listorder)-1
    while left<=right:
        mid=(left+right)//2
        if listorder[mid]<num:
            left=mid+1
        elif listorder[mid]>num:
            right=mid-1
        else:
            return mid
    return -1
if __name__=='__main__':
    li=[5,7,13,25,32,46,78,87]
    print  binarysearch(li,25)
  
#�ݹ�
def binarysearch2(li,num,left,right):
    mid=(left+right)//2
    if num==li[mid]:
        return mid
    else:
        if (num>li[mid]):
            left=mid+1
        elif (num<li[mid]):
            right=mid-1
        return binarysearch2(li, num, left, right)
if __name__=='__main__':
    li=[5,7,13,25,32,46,78,87]
    print  binarysearch2(li,25,0,7)
        
    
    
        
    