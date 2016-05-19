def drawPoint(start,end):
    for i in (start,end+1):
        print "*"
        for j in (start+1,end):
        print " "
def drawLine(start,end):
    for i in (start,end):
    print "*"

a = 1,4,9
b = 5,6,7
c = 2
d = 3
for i in a:
    print drawLine(0,5)
    for i in c:
        print drawPoint(1,3)
        for i in d:
            print drawPoint(2,2)
            for i in b:
                print drawPoint(0,5)
