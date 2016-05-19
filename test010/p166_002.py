#-*-coding:utf-8-*-
'''
Created on 2015年5月5日
Description:第166页第2题
@author:ECNU_zenwan
@version:1.0
'''
import time
import sys
import os
opened=False
fine=False
while True:
    try:
        filename=raw_input('输入账单文件名：')
        f = open(filename)
        opened=True
        sum=0
        i=0 #行号
        while True: # 常用的读取文件的习惯
            i+=1
            Number = f.readline()
            if len(Number) == 0: #文件结束
                break
            elif len(Number.strip()) == 0: #读取的是空行
                continue
            else:
                Number=float(Number)
                time.sleep(1)
                print('%.2f + %.2f =%.2f'%(sum,Number,sum+Number))
                sum+=Number
    except KeyboardInterrupt:
        print('你是如此的没有耐心，按了Ctrl+C，程序被你中断了！')
        sys.exit()
    except IOError:
        print('%s 文件不存在！请重新输入文件名！'%filename)
    except ValueError:
        print('%s 文件中第 %d 行含有无效数字[%s]，请修改该文件后再来！'%(filename,i,Number))
        sys.exit()
    else:
        fine=True
        break
    finally:
        if opened:
            f.close()
            print('\n打开的 %s 文件被关闭了！'%filename)
if fine:
    print('总和为 %f'%sum)
print('结束!')
    