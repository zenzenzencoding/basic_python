OldList=[10,2,3,13,2,44,2,10]
NewList=[]
NewList.append(OldList[0])
for i in range  (len(OlidList)):
    for j in range(len(NewList)):
        if NewList[j]!=OldList[i]:
            flag=False
            break
        else:
            flag=True
    if flag=True:
        NewList.append(Oldlist[i])
print('原列表为：',OldList)
print('新列表为：',NewList)

