def drawPoint(start,end):#在start和end位置上打印两个星号（允许start和end位置重合）
    if start==end:
        a=start
        print((a-1)*" "+"*")
    else:
        a=start
        b=end
        print((a-1)*" "+"*"+(b-a-1)*" "+"*")
def drawLine(start,end):#从start开始到end结束，打印一条连续星号构成的线段
    if start==end:
        a=start
        print((a-1)*" "+"*")
    else:
        a=start
        b=end
        print((a-1)*" "+(b-a+1)*"*")

drawLine(1,5)
drawPoint(2,4)
drawPoint(3,3)
drawLine(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawPoint(1,5)
drawLine(1,5)
