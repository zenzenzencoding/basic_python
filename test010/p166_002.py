#-*-coding:utf-8-*-
'''
Created on 2015��5��5��
Description:��166ҳ��2��
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
        filename=raw_input('�����˵��ļ�����')
        f = open(filename)
        opened=True
        sum=0
        i=0 #�к�
        while True: # ���õĶ�ȡ�ļ���ϰ��
            i+=1
            Number = f.readline()
            if len(Number) == 0: #�ļ�����
                break
            elif len(Number.strip()) == 0: #��ȡ���ǿ���
                continue
            else:
                Number=float(Number)
                time.sleep(1)
                print('%.2f + %.2f =%.2f'%(sum,Number,sum+Number))
                sum+=Number
    except KeyboardInterrupt:
        print('������˵�û�����ģ�����Ctrl+C���������ж��ˣ�')
        sys.exit()
    except IOError:
        print('%s �ļ������ڣ������������ļ�����'%filename)
    except ValueError:
        print('%s �ļ��е� %d �к�����Ч����[%s]�����޸ĸ��ļ���������'%(filename,i,Number))
        sys.exit()
    else:
        fine=True
        break
    finally:
        if opened:
            f.close()
            print('\n�򿪵� %s �ļ����ر��ˣ�'%filename)
if fine:
    print('�ܺ�Ϊ %f'%sum)
print('����!')
    