﻿def guest(s): #形参s表示身份证倒数第2位
    if s/2==0:
        return "女士"
    else:
        return "先生"
id=input("请输入客户的身份证号:\n")
year=#客户出生年份
mf=id(17,17)#身份证倒数第2位
print("该%s出生于%s年"%(s,year))


