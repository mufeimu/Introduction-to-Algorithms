#!/usr/bin/env python
# coding: utf-8


class SqList:
    def __init__(self):
        self.SqList=[]
    def CreateSqList(self):
        Element = input("请输入（按回车键确认并继续输入，按#键结束）：")
        while Element !='#':
            self.SqList.append(Element)
            Element=input("请输入（按回车键确认并继续输入，按#键结束）：")
        return self.SqList
    def ListInsert(self):
        pos=int(input("请输入要插入的位置:"))
        key=input("请输入要插入的值:")
        print('插入前顺序表为：\n',self.SqList)
        if pos < len(self.SqList) and pos >= 0:
            self.SqList.insert(pos-1,key)
            return self.SqList
        else:
            print('错误！插入位置要在列表长度之内哦！！！')   
    def ListDelete(self):
        pos=int(input("请输入要删除的位置:"))
        print('删除前顺序表为：\n',self.SqList)
        if pos < len(self.SqList) and pos >= 0:
            del self.SqList[pos-1]
            return self.SqList
        else:
            print('错误！删除位置要在列表长度之内哦！！！') 
    def length(self):
        return len(self.SqList)
    def content(self):
        return self.SqList
list_1 = SqList()
print('顺序表初始化为:',list_1.CreateSqList())
print('插入后的顺序表：\n',list_1.ListInsert())
print('删除后的顺序表：\n',list_1.ListDelete())
print("该顺序表的内容为:",list_1.content())
print("该顺序表的长度为:",list_1.length())
