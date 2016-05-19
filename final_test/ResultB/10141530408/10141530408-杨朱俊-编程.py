def drawPoint(a,b):
    s=''
    if a > b:
        a,b=b,a
    if a < b:
        s=' '*(a-1)+'*'+' '*(b-a-1)+'*'
    else:
        s=' '*(a-1)+'*'
    print(s)
def drawLine(a,b):
    s=''
    if a > b:
        a,b=b,a
    s=' '*(a-1)+'*'*(b-a+1)
    print(s)
print('')
drawLine(1,5)
print(' ')
drawPoint(2,4)
print('')
drawPoint(3,3)
print('')
drawLine(1,5)
print('')
drawPoint(1,5)
print('')
drawPoint(1,5)
print('')
drawPoint(1,5)
print('')
drawLine(1,5)

    
