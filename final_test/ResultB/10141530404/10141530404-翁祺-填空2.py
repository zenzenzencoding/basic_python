def BinarySearchPst(a, target):
    low = 0 
    high = len(a)
    while low <= high:
        mid = int((high-low)/2)+1
        midVal = a[mid] 
        if midVal < target: 
            a.remove()
        elif midVal > target: 
            high = mid - 1 
        else: 
            return '查找到该数，所在位置为：'+repr(low+mid+1)
    return '该数不在列表中'
Ldata = [17,19,25,37,42,51,67,86,99]
x=int(input('请输入要查找的一个整数：'))
print(BinarySearchPst(Ldata,x))
