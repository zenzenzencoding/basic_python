def drawPoint(start,end):
    if int(end)>int(start):
        print((int(start)-1)*' '+'*'+(int(end)-int(start)-1)*' '+'*')
    else:
        print((int(start)-1)*' '+'*')
def drawLine(start,end):
    print((int(start)-1)*' '+(int(end)-int(start)+1)*'*')
print('\n')
drawLine(1,5)
drawPoint(2,4)
drawPoint(3,3)
drawLine(1,5)
drawPoint(2,4)
drawPoint(2,4)
drawPoint(2,4)
drawLine(1,5)



    

