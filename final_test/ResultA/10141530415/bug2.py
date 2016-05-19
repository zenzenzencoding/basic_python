f=open('cusinfo.txt')
List1=[]
for i in f :
    List1.extend(i.split())
List2=[]
for i in range(1,len(List1)-1,3):
    if List1[i]=='女':
        List2.append(List1[i-1])
print(List2)
        
            
    


