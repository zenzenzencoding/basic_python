def calc(s,n):
    h=s/2
    for i in range(2,n):
        s=s+h
        h=h/2
    return(s)
x=int(input("请输入小球初始高度："))
y=int(input("请输入所求第几次落地后："))
sn=calc(x,y)#表示小球共经过了多少米
print("高度为%d米的小球，第%d次落地后共经过%.3f。"%(x,y,sn))
