#!/usr/bin/env python
# coding: utf-8

# In[34]:


# 创建结点类
class ListNode(object):
    def __init__(self,data):
        self.data=data
        self.next=None

#创建链表类
class CreateLinkList(object):
    def __init__(self):
        self.head=ListNode(None)
    #链表初始化函数，将data的值输入到链表中
    def initList(self,data):
         # 创建头结点
        self.head=ListNode(data[0])
        p=self.head
        for i in data[1:]:
            node=ListNode(i)
            p.next=node
            p=p.next
        return self.head#缺失该语句，会造成initList()类型不是链表类型，而是NoneType；链表类型__main__.LNode


#遍历链表，输出链表函数
def ReadList(L):
    p = L
    while p:
        print(p.data,end="-->")
        p=p.next
    print('')
#有序链表合并函数
def MergeList(La,Lb):
    pa = La
    pb = Lb
    if pa.data<= pb.data:
        Lc = pc = pa
        pa = pa.next 
    else:
        Lc = pc = pb
        pb = pb.next
    while pa and pb:
        if pa.data <= pb.data:
            pc.next = pa
            pc = pa
            pa = pa.next 
        else:
            pc.next = pb 
            pc = pb
            pb = pb.next
    if pb:
        pc.next = pb
    if pa:
        pc.next = pa
    return Lc  
if __name__ == '__main__':
    data1=[2,5,8]
    data2=[3,5,7,9]
    
    l=CreateLinkList()
    La=l.initList(data1)
    Lb=l.initList(data2)
    Lc= MergeList(La,Lb)
    ReadList(Lc)

