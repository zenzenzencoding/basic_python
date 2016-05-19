def drawPoint(start,end):
    s=''
    for i in range(0,end+1):
        if i==start or i==end:
            s=s+'*'
        else:
            s+=''
    return s
def drawLine(start,end):
    s=''
    for i in range(start,end):
        if i>=start and i<=end:
            s=s+'*'
    return s
print(drawLine(0,5))
print(drawPoint(1,3))
print(drawPoint(2,2))
print(drawLine(0,5))
print(drawPoint(0,5))
print(drawPoint(0,5))
print(drawPoint(0,5))
print(drawLine(0,5))
