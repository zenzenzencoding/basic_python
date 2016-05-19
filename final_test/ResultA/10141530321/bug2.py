f=open('cusinfo.txt')
b=f.read()
c=b.split('\n')
List1=[]
for i in c :
    li=list(i)
    List1.append(i.split("\t"))
f.close()
List2=[]
for i in range(0,len(List1)):
    a=List1[i]
    if a[1]='女':
        List2.append(a[0])
print(List2)
        
            
    


