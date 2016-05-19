def drawPoint(start,end):
    if start!=end:
        print(' '*start+'*'+' '*(end-start-1)+'*')
    else:
        print(' '*(start-1),'*')
def drawLine(start,end):
    print(' '*start+'*'*(end-start+1))
drawLine(0,4)
drawPoint(1,3)
drawPoint(2,2)
drawLine(0,4)
drawPoint(0,4)
drawPoint(0,4)
drawPoint(0,4)
drawLine(0,4)
