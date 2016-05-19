def guest(s):
    if s%2==0:
        return "女士"
    else:
        return "先生"
id=input("请输入客户的身份证号:\n")
year=id[6:10]
mf=int(id[16:17])
print("该%s出生于%s年"%(guest(mf),year))
