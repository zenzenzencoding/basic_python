OldList=[10,2,3,13,2,44,2,10]
NewList=[]
NewList.append(OldList[0])
for i in range(1,len(OldList)-1):
    for j in range(len(NewList)):
        if OldList[i]==NewList[j]:
            flag=False
            break
        else:
            flag=True
    if flag:
        NewList.append(OldList[i])
print('原列表为：',OldList)
print('新列表为：',NewList)

