def drawPoint(a,b):
    for i in range (a,b+1):
        if i==a:
            print("*",drawPoint(a,b))
        elif i==b:
            print("*",drawPoint(a,b))
        else:
            print("",drawPoint(a,b))
    return drawPoint(a,b)
def drawLine(start,end):
    for i in range (start,end):
        a+=1
        print("*"*a, drawLine(start,end))
start=int(input("start="))
end=int(input("end="))

