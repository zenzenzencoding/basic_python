f=open('cusinfo.txt','r')
List1=[]
for i in f:
    List1.append(f.split())
List2=[]
for i in range(0,len(List1)):
    if List1[i][1]=='女':
        List2.append(List1[i][0])
print(List2)
        
            
    


