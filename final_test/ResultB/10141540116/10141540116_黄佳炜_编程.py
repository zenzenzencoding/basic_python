def drawLine(start,end):
    print('*'*(end-start+1))
def drawpoint(start,end):
    if start==end:
        print(' '*start+'*')
    else:
        print(' '*(start)+'*'+' '*(end-start-1)+'*')
def Triangle():
    drawLine(0,4)
    drawpoint(1,3)
    drawpoint(2,2)
    drawLine(0,4)
    drawpoint(0,4)
    drawpoint(0,4)
    drawpoint(0,4)
    drawLine(0,4)
