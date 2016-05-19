def drawPoint(start,end):
    for i in range(0,start):
        for j in range(start+1,end):
            print('')
    else:
        print('*')
a=int(input('请输入起始点：'))
b=int(input('请输入终点：'))
drawPoint(a,b)
