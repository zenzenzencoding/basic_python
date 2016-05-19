#-*-coding:utf-8-*-
'''
Created on 2015年5月12日
Description：小王希望用电脑记录他每天掌握的英文单词。请设计程序和相应的数据结构，
使小王能记录新学的英文单词和其中文翻译，并能很方便地根据英文来查找中文。
@author:ECNU_zenwan
@version：
'''
dic={}
while True:
    print("请选择功能：\n1: 输入\n2：查找\n3：退出")
    c=raw_input()
    if c=="1":
        word=raw_input("请输入英文单词（按回车结束）：")
        if len(word)==0:
            break;
        meaning=raw_input("请输入中文翻译：")
        dic[word]=meaning
        print("该单词已添加到字典库。")

    elif c=='2':
        word=raw_input("请输入要查询的英文单词（按回车结束）：")
        if len(word)==0:
            break;
        if word in dic:
            print("%c的中文翻译是%c"%(word,dic[word]))
        else:
            print("字典库中未找到这个单词")

    elif c=="3":
        break
    else:
        print("输入有误！")
        continue
