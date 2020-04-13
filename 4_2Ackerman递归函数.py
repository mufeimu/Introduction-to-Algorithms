"""
非递归方法实现Ackman函数
"""
class SStack(object):
    #初始化栈为空列表
    def __init__(self):
        self.items=[]
    #判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items==[]
    #返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]
    #输出栈内容并返回栈的大小
    def deep(self):
        return len(self.items)
    #把新的元素堆进栈里
    def push(self,data):
        return self.items.append(data)
    #把栈顶元素弹出
    def pop(self):
        return self.items.pop()
def Ackerman_stack(m,n):
    st1=SStack()
    st2=SStack()
    st1.push(m)
    st2.push(n)
    while m!=0:
        if n!=0:           ##当m!=0以及n!=0时
            st1.push(m)
            n-=1
            st2.push(n)
        elif n==0:        ##当m!=0以及n==0时
            m=st1.pop()-1
            n=1
            st2.pop()
            st1.push(m)
            st2.push(1)
        while m==0 and st2.deep()>1:   ##当m==0时
            st1.pop()
            n=st2.pop()
            m=st1.pop()
            st2.pop()
            m-=1
            n+=1
            st1.push(m)
            st2.push(n)
    return (st2.pop() + 1)
print('Ackerman(3,4)=',Ackerman_stack(3,4))
