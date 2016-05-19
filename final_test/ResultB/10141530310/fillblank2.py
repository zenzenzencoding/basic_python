_______________(a, target):
    low = 0 
    high = ____________
    while low <= high:
        mid = _______________ 
        midVal = a[mid] 
        if midVal < target: 
            _________________ 
        elif midVal > target: 
            high = mid - 1 
        else: 
            return '查找到该数，所在位置为：'+__________
    return '该数不在列表中'
Ldata = [17,19,25,37,42,51,67,86,99]
x=int(input('请输入要查找的一个整数：'))
print(BinarySearchPst(Ldata,x))
