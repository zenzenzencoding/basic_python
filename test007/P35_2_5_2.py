#-*-coding:utf-8-*-
a,b,c=0,0,0
def chibin(n):
    global a,b,c
    s=0
    if a==0:
        if n>=2:
            a=2
            print("A��2����")
            n=n-2
            s=s+2
        elif n<=1:
            a=1
            print("A��1����")
            n=n-1
            s=s+1
            return s
    if b==0:
        if n>=2:
            b=input("BҪ�Լ�����:")
            c=b
        elif n==1:
            b=1
            c=b
            print("B����1����")        
    a=a-1
    b=b-1
    if (n-c)<=0:
        return s
    else:
        return s+chibin(n-c)
if __name__=="__main__":
    n=input("�����������:")
    print "Aһ������:%d��"%(chibin(n))
            
        