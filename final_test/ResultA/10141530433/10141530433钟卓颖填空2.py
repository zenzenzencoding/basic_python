OldList=[10,2,3,13,2,44,2,10]
NewList=[]
NewList.append(OldList[0])
for i in range str(OldList):
    for j in range(len(NewList)):
        if j==2:
            flag=False
            break
        else:
            flag=True
    if True:
        NewList.append(j)
print('原列表为：',OldList)
print('新列表为：',NewList)

