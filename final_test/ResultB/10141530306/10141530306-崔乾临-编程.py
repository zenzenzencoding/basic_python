def drawPoint(start,end):
    i = 1 #起点坐标初始化为1
    pic = "" #待打印字符串初始化为空
    while i <= end:
        if i == start or i == end:
            pic += "*" #起点和终点打印*
        else:
            pic += " " #其它点打印空格
        i = i + 1 #坐标位置向右移动一格直至终点
    return pic
def drawLine(start,end):
    i=1 #起点坐标初始化为1
    pic="" #待打印字符串初始化为空
    while i<=end:
        if start <= i <= end:
            pic+="*" #起点和终点之间打印*
        else:
            pic+=" " #起点之前打印空格
        i = i + 1 #坐标位置向右移动一格直至终点
    return pic
for i in range(1,18): #打印内容在1到17行之间
    if i%2==1:
        print() #奇数行为空
    else:
        if i==4 or i==6:
            print(drawPoint(i/2,6-i/2))
        elif 10 <= i <=14:
            print(drawPoint(1,5))
        else:
            print(drawLine(1,5)) #偶数行分成三种情况打印*
