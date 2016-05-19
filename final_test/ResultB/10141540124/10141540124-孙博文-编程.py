def drawPoint(start,end):
    l=start*' '+'*'+' '*(end-start-1)+'*'
    return l
def drawLine(start,end):
    s=start*' '+'*'*(end-start+1)
    return s
print(drawLine(0,4))
print(drawPoint(1,3))
print(drawLine(2,2))
print(drawLine(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawLine(0,4))
