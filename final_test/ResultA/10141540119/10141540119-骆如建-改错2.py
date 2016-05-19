f=open('cusinfo.txt')
List1=[]
for i in f.read():
    List1.extend(i.split())
    print(List1)
List2=[]
for j in range(1,len(List1)+1):
    if List1[j][2]=='女':
        List2.append(List1[i][0])
print(List2)
        
            
    


