def drawPoint(start,end):
    if start!=end:
        print((start-1)*'','*',(end-start-1)*'','*')      
    else:
        print((start-1)*'','*')
    return''
def drawLine(start,end):
    print((start-1)*'',(end-start+1)*'*')
    return''
print(drawLine(1,5))
print(drawPoint(2,4))
print(drawPoint(3,3))
print(drawLine(1,5))
print(drawPoint(1,5))
print(drawPoint(1,5))
print(drawPoint(1,5))
print(drawLine(1,5))

    
