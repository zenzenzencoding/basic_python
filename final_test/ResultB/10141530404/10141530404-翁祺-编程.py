def drawPoint(start,end):
    if start!=end:
        return(' '*(start-1)+'*'+' '*(end-start-1)+'*')
    else:
        return(' '*(start-1)+'*')
def drawLine(start,end):
    return(' '*(start-1)+'*'*(end-start+1))
print(drawLine(1,5))
print(drawPoint(2,4))
print(drawPoint(3,3))
print(drawLine(1,5))
print(drawPoint(1,5))
print(drawPoint(1,5))
print(drawPoint(1,5))
print(drawLine(1,5))
