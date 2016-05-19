#不连续的*
def drawPoint(start,end):
    for j in range(0,end+1):
         if j==start or j==end:
                print('*')
        else:
            print(' ')
    return


#连续的*
def drawLine(start,end):
    for j in range(0,end+1):
        if start<=j and end>=j:
            print('*')
        else:
            print(' ')
    return
print(drawLine(1,5)/n+drawPoint(2,4)/n+drawPoint(3,3)/n+drawLine
