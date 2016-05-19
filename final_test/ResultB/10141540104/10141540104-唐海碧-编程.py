def drawPoint(a,b):
    if a==b:
        s=' '*a+'*'
    else:
        s=' '*a+'*'+int(b-a-1)*' '+'*'
    return s
def drawLine(a,b):
    s=int(b-a+1)*'*'
    return s
print(drawLine(0,4))
print(drawPoint(1,3))
print(drawPoint(2,2))
print(drawLine(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawPoint(0,4))
print(drawLine(0,4))
