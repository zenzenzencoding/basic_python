def drawPoint(start,end):
    if end>start:
        print(' '*start+'*'+' '*(end-start-1)+'*')
    elif end==start:
        print(' '*start+'*')
def drawLine(start,end):
    print('*'*(end-start+1))
drawLine(0,4)
drawPoint(1,3)
drawPoint(2,2)
drawLine(0,4)
for i in range(0,3):
    drawPoint(0,4)
drawLine(0,4)
