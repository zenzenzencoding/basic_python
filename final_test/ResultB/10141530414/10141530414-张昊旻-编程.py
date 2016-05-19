def drawPoint(start,end):
    a=' '*(start-1)+'*'+' '*(end-start-1)+'*'
    return a
def drawLine(start,end):
    b='*'*(end-start+1)
    return b
for i in range (1,9):
    if i==1 or i==4 or i==8:
        print(drawLine(1,5))
    elif i==2:
        print(drawPoint(2,4))
    elif i==3:
        print('  *  ')
    else:
        print(drawPoint(1,5))
