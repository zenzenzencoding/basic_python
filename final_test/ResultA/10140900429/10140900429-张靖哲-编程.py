#encoding:utf-8
def intToBinArr( x ): 
    R=''
    while x!=0:
        temp = x % 2 #���ֳ���2������
        R = x // 2  #���ֳ���2������������
        R=str(temp)+str(R)
    return R
#x=int(input('������һ����������'))
print( '123',intToBinArr(25)) 
        
    
