f=open('cusinfo.txt')
a=readlines.f
List1=[]
for i in a:
    List1.append(i.split())
List2=[]
for i in range(0,len(List1)):
    if List1[i][1]=='女':
        List2.append(List1[i][0])
print(List2)
        
            
    


