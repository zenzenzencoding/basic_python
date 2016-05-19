def drawPoint(start,end):
    s=''
    for i in range(0,5):
        if i==start:
            s+='*'
        elif i==end:
            s+='*'
        else:
            s+=' '
    return s
def drawLine(start,end):
    s=''
    for i in range(start,end+1):
        s+='*'
    return s
print(drawLine(0,4))
print(drawPoint(1,3))
print(drawPoint(2,2))
print(drawLine(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawLine(0,4))
