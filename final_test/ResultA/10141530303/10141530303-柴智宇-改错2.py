f=list(open('cusinfo.txt'))
List1=[]
for i in range (0, len(f)):
    List1.extend(f[i].split())
List2=[]
for i in range(0,len(List1)):
    if List1[i]=='女':
        List2.append(List1[i-1])
print(List2)
        
            
    


