#-*-coding:utf-8-*-
'''
Created on 2015年5月5日
Description：第165页第一题
@author:ECNU_zenwan
@version：1.0
'''
import math
error_num=-1
class MyException(Exception):#自定义异常
    pass
while True:
    error_num+=1
    try:
        a=float(input("输入a:"))
        b=float(input("输入b:"))
        if a<b or a<20 or b<20:
            raise MyException(a,b)
        result1=a/(a-b-1)
        result2=math.sqrt(a**2-b**2)
        result3=a**b
    except MyException as e:
            print ("第一个数字必须大于第二个数字，且均大于20")            
    except ZeroDivisionError:
        print ("你见过除数是零的吗？")       
    except ValueError:
        print ("请使用半角的阿拉伯数字！")       
    except KeyboardInterrupt:
        print("你自己中断了程序")       
    except EOFError:
        print("没事别乱按Ctrl+Z")
    except OverflowError:
        print("超出python支持的最大的数字")       
    except:
        print("其它未知错误！")       
    else:
        break
    finally:
        if error_num!=0:
            print("你已经犯了%d次错了")%(error_num)
print("a/(a-b-1)=%.2f\nmath.sqrt(a**2-b**2)=%.2f\na**b=%.2f\n")%(result1,result2,result3)
print("恭喜圆满完成任务，辛苦啦，喝杯茶，继续下一题！！")    
    