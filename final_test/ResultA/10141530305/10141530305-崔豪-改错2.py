f=open('cusinfo.txt')
List1=[]
for i in f:
    List1.extend(i.split())
List2=[]
for i in range(0,len(List1)):
    if List1[1][i]=="女":
        List2.append(List1[0][i])
print(List2)
f.close
        
            
    


