#-*-coding:utf-8-*-
'''
Created on 2015年5月26日
Description：005
@author:ECNU_zenwan
@version：
'''
def drawPoint(start,end):
    if(start==end):
        print(" "*(start-1)+"*")
    else:
        print(" "*(start-1)+"*"+' '*(end-start-1)+'*')

def drawCilrcle():
    drawPoint(3,5)
    drawPoint(2,6)
    drawPoint(3,5)
   
def drawInsect():
    drawPoint(4,4)
    drawPoint(3,5)
    drawPoint(2,6)
    
def drawRectangle():
    drawPoint(1,7)
    drawPoint(1,7)
    drawPoint(1,7)
    drawPoint(1,7)
    drawPoint(1,7)
def drawTriangle():
    drawInsect()
    drawPoint(3,5)
#画出女孩
drawCilrcle()
drawTriangle()
drawInsect()