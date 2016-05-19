s=input("请输入一个字符串:\n")
s2=s.lower
fomart=[a,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9]
for c in s2:
    if c in fomart:
        s2=s2
    else:
        s2=s2.replace(c,'')
print("只保留英文和数字后的字符串为："+s2)
