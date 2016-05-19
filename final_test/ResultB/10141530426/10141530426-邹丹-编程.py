s='*'
b=' '
def drawPoint(start,end):
    if start!=end:
        m=b*(start-1)+s+b*(end-start-1)+s
    else :
        m=b*(start-1)+s
    print(m)    
def drawLine(start,end):
    n=s*(end+1-start)
    print(n)
drawLine(1,5)
drawPoint(2,4)
drawPoint(3,3)
drawLine(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawLine(1,5)
