def drawLine(start,end):
    print(" "*(start-1)+"*"*(end-start+1))
def drawPoint(start,end):
    if start==end:
        print(" "*(start-1)+"*")
    else:
        print(" "*(start-1)+"*"+" "*(end-start-1)+"*")

def drawTri():
    drawLine(1,5)
    drawPoint(2,4)
    drawPoint(3,3)
def drawRec():
    drawLine(1,5)
    drawPoint(1,5)
    drawPoint(1,5)
    drawPoint(1,5)
    drawLine(1,5)
drawTri()
drawRec()
