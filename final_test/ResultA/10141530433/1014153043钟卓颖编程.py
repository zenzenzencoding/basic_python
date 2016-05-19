def cal(n):
    value=0
    for count in range(1,n+1,2):
        value+=count
    return value
n=int(input("请输入一个 n="))
print('和为',cal(n))
s=[]
if n>=1:
    s+=cal(n)
else:
        print("输出错误")
print("和为：",s)

