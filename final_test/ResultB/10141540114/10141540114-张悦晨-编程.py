def drawPoint(start,end):
    start=int(start)
    end=int(end)
    for i in range(start,start+1):
        print("*")
    for j in range(end,end+1):
        print("*")

def drawLine(start,end):
    start=int(start)
    end=int(end)
    print('*'*(end-start))
drawLine(1,6)
drawPoint(1,6)
