def drawPoint(start,end):
    s=''
    for i in range(10):
        if start==i:
            s+='*'
        elif end==i:
            s+='*'
        else:
            s+=' '
    return(s)
def drawLine(start,end):
    s=''
    for i in range(0,start):
        s+=' '
    for i in range(start,end):
        s+='*'
    return(s)
print(drawLine(0,5))
print(drawPoint(1,3))
print(drawLine(2,3))
print(drawLine(0,5))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawLine(0,5))
