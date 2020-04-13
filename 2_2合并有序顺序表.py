#!/usr/bin/env python
# coding: utf-8

# In[2]:


def MergeList(l1,l2):                               #定义一个合并列表的函数
    l3 = [' ' for i in range(len(l1)+len(l2))]     #构建一个长度为两个列表长度之和的新列表l3，l3列表里全是空格元素
    i=j=0
    k=0
    while(i<=len(l1)-1 and j<=len(l2)-1):       # 分别设置l1和l2的指针为i,j，当指针小于l1和l2的列表长度时才执行
        if l1[i]<=l2[j]:                         #将l1和l2中较小的值放入l3中
            l3[k]=l1[i]
            i+=1
            k+=1
        else:
            l3[k]=l2[j]
            j=j+1
            k=k+1
    while i<=len(l1)-1:                       #如果l1未比较完，将l1剩下的全部放入l3
            l3[k]=l1[i]
            i=i+1
            k=k+1
    while j<=len(l2)-1:                      #如果l2未比较完，将l1剩下的全部放入l3
        l3[k]=l2[j]
        j=j+1
        k=k+1
    return l3
l1=[3,5,7,16]
l2=[2,6,7,18,21]
print(MergeList(l1,l2))


# In[ ]:




