def cal(n):
    s=0
    sn=0
    for n in range(1,12,2):
        if n<=11:
            s=s+n
            sn=sn+s
    return sn
print('总和为：',sn)
        
        
        
