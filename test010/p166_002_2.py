#-*-coding:utf-8-*-
'''
Created on 2015��5��5��
Description: ��2��
@author:ECNU_zenwan
@version: 1.0
'''
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
        filename=raw_input('�����˵��ļ�����')#E:\document\�����ĵ�\ch5\�ı��ļ�\data11.txt
        f = open(filename)
        opened=True
        sum=0
        Number= f.readlines()
        for i in range(len(Number)): 
            if len(Number[i]) == 0: #��ȡ���ǿ���
                continue
            else:
                Number[i]=float(Number[i])
                time.sleep(1)
                print('%.2f + %.2f =%.2f'%(sum,Number[i],sum+Number[i]))
                sum+=Number[i]
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
    