def drawPoint(start,end):
    if start==end:
        print((start-1)*' '+'*')
    else:
        print((start-1)*' '+'*'+(end-start-1)*' '+'*')
    return
def drawLine(start,end):
    print((start-1)*' '+(end-start+1)*'*')
    return
drawLine(1,5)
drawPoint(2,4)
drawPoint(3,3)
drawLine(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawLine(1,5)
