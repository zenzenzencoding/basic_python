#-*-coding:utf-8-*-
'''
Created on 2015��5��12��
Description��С��ϣ���õ��Լ�¼��ÿ�����յ�Ӣ�ĵ��ʡ�����Ƴ������Ӧ�����ݽṹ��
ʹС���ܼ�¼��ѧ��Ӣ�ĵ��ʺ������ķ��룬���ܷܺ���ظ���Ӣ�����������ġ�
@author:ECNU_zenwan
@version��
'''
dic={}
while True:
    print("��ѡ���ܣ�\n1: ����\n2������\n3���˳�")
    c=raw_input()
    if c=="1":
        word=raw_input("������Ӣ�ĵ��ʣ����س���������")
        if len(word)==0:
            break;
        meaning=raw_input("���������ķ��룺")
        dic[word]=meaning
        print("�õ�������ӵ��ֵ�⡣")

    elif c=='2':
        word=raw_input("������Ҫ��ѯ��Ӣ�ĵ��ʣ����س���������")
        if len(word)==0:
            break;
        if word in dic:
            print("%c�����ķ�����%c"%(word,dic[word]))
        else:
            print("�ֵ����δ�ҵ��������")

    elif c=="3":
        break
    else:
        print("��������")
        continue
