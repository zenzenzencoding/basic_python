s=input("请输入一个字符串:\n")
s2 = list(s.lower)
fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
for c in s2:
    while c in fomart:
        s2 = s.replace(c,'')  
print("只保留英文和数字后的字符串为：",s2)
