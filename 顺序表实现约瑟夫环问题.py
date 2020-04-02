#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
算法思想：刚开始把所有的人放到一个列表里面去，不是退圈的报数数字就把这个人放到列表的最后
一个位置上面去，如果是退圈的报数数字就把这个数字从列表中去掉。直到列表剩下最后一个人为止
"""
def josephus():
    #n代表总人数，k代表退圈的报数数字
    n=int(input("请输入总人数n:"))
    m=int(input("请输入退圈的报数数字m:"))
    l1 = list(range(1,n+1))  #将所有人放入列表
    l2=[]                    #设置一个空列表，用来存放退圈的顺序
    index = 0                #设置计数器，以便测试是否到达退圈的报数数字
    while l1:
        temp = l1.pop(0)
        index += 1
        if index == m:       #如果计数器到达退圈的报数数字，L2列表便增加该元素，并将计数器归0
            l2.append(temp)
            index = 0
            continue
        l1.append(temp)    #将这个人放到列表的最后一个位置上
        if len(l1)==1:    #如果列表只剩下最后一个元素，则运算停止，输出L2，退圈的顺序
            l2.append(l1[0])
            return l2
            break

print("最终的退圈顺序为：\n",josephus())


# In[ ]:




