def cal(n):                  #此处定义函数cal(n)
    s=0
    a=1
    while a<=n:
        s=s+a
        a=a+2
    return s                 #利用函数cal(n)计算数列各项的值
sn=0                         #以下为主程序
for n in range(1,13,2):      #通过循环结构调用上述函数进行数列的求和
    sn=sn+cal(n)
print("总和为：",sn)          #输出最终的运行结果
