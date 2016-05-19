def drawpoint(start,end):
    if start==end:
        s=' '*(start-1)+'*'
    else:
        s=' '*(start-1)+'*'+' '*(end-start-1)+'*'
    return s
def drawline(start,end):
    s=' '*(start-1)+'*'*(end-start+1)
    return s
print(drawline(1,5))
print(drawpoint(2,4))
print(drawpoint(3,3))
print(drawline(1,5))
print(drawpoint(1,5))
print(drawpoint(1,5))
print(drawpoint(1,5))
print(drawline(1,5))
