#-*-coding:utf-8-*-
'''
Created on 2015��5��5��
Description����165ҳ��һ��
@author:ECNU_zenwan
@version��1.0
'''
import math
error_num=-1
class MyException(Exception):#�Զ����쳣
    pass
while True:
    error_num+=1
    try:
        a=float(input("����a:"))
        b=float(input("����b:"))
        if a<b or a<20 or b<20:
            raise MyException(a,b)
        result1=a/(a-b-1)
        result2=math.sqrt(a**2-b**2)
        result3=a**b
    except MyException as e:
            print ("��һ�����ֱ�����ڵڶ������֣��Ҿ�����20")            
    except ZeroDivisionError:
        print ("����������������")       
    except ValueError:
        print ("��ʹ�ð�ǵİ��������֣�")       
    except KeyboardInterrupt:
        print("���Լ��ж��˳���")       
    except EOFError:
        print("û�±��Ұ�Ctrl+Z")
    except OverflowError:
        print("����python֧�ֵ���������")       
    except:
        print("����δ֪����")       
    else:
        break
    finally:
        if error_num!=0:
            print("���Ѿ�����%d�δ���")%(error_num)
print("a/(a-b-1)=%.2f\nmath.sqrt(a**2-b**2)=%.2f\na**b=%.2f\n")%(result1,result2,result3)
print("��ϲԲ������������������ȱ��裬������һ�⣡��")    
    