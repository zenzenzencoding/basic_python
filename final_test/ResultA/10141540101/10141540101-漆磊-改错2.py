f=open('C:\\ECNU_KS\\root\\cusinfo.txt','r')
List1=[]
a=f.readlines()
for i in range(0,len(a)):
    List1.extend([a[i].split()])
List2=[]
for i in range(0,len(List1)):
    if List1[i][1]=='女':
        List2.append(List1[i][0])
print(List2)
        
            
    


