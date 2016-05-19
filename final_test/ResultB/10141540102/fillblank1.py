def guest(s): #形参s表示身份证倒数第2位
    if mf%2==0:
        return "女士"
    else:
        return "先生"
id=input("请输入客户的身份证号:_______")
k=int(id)-int(id)//1000000000000*1000000000000


year=k//100000000#客户出生年份
mf=(int(id)//10*10-int(id)//100*100)//10#身份证倒数第2位
print("该%s出生于%s年"%(guest(mf),year))


