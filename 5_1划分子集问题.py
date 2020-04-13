class SQueue(object):
    def __init__(self):
        self.head=0
        self.rear=0
        self.items=[0]*MAXQSIZE
    def is_empty(self):
        return self.rear==self.head
    #输出队列内容及返回队列大小
    def size(self):

        if self.rear>=self.head:
            content=self.items[self.head:self.rear]
            length=len(self.items[self.head:self.rear])
            return content,length
        else:
            content=self.items[self.head:],self.items[:self.rear]
            length=len(self.items[self.head:]+self.items[:self.rear])
            return content,length
    def enqueue(self,item):
        if int(self.rear+1)%MAXQSIZE==self.head: #判断队列是否满
            return 'the queue is full'
        self.items[self.rear]=item
        self.rear=int(self.rear+1)%MAXQSIZE #队尾指针后移
    def dequeue(self):
        if self.rear==self.head: #判断队列是否空
#             print('the queue is empty')
            return 'the queue is empty'
        e=self.items[self.head]
        self.head=int(self.head+1)%MAXQSIZE #对头指针后移
        return e 

def division(R,cq):  #形参R需输入冲突关系矩阵、形参n需输入队列元素个数
    res=[]
    x,n=cq.size()
    pre=n
    while cq.is_empty()==False:
        cur=cq.dequeue()   #头元素出队列
#         print('cur:',cur)
        if pre>=int(cur):      #是否需要创建新的空子集
            res.append([])
#             print('res:',res)
            
        #检查当前的数是否与子集内的数有冲突
        for a in res[-1]:
            if R[cur-1][a-1]:#有冲突
#                 print('有冲突的元素:',cur)
                cq.enqueue(cur)  #重新放入队列尾部
                break
        else:#没有冲突
            res[-1].append(cur)
        print('无冲突的子集：',res)
        pre=cur #当前变成之前的
#         print('目前的pre:',pre)
        x,y=cq.size()
#         print('cq的：',x)
    return res
 
if __name__=='__main__':
    MAXQSIZE=10
    #初始化队列对象
    import numpy as np
    cq=SQueue()
    A={1,2,3,4,5,6,7,8,9}
    Rel=((2,8),(9,4),(2,9),(2,1),(2,5),(6,2),(5,9),(5,6),(5,4),(7,5),(7,6),(3,7),(6,3))
    R=np.random.randint(0,1,size=[9,9])  #随机生成9行9列全为0的二维数组
    for i in Rel:
        if i[0]!=0 and i[1]!=0:
            R[i[0]-1,i[1]-1]=1
            R[i[1]-1,i[0]-1]=1
#     print('该循环队列最大空间MAXQSIZE为:',MAXQSIZE)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    cq.enqueue(7)
    cq.enqueue(8)
    cq.enqueue(9)
    print('队列的内容和大小:',cq.size())
    result=division(R,cq)
    print('最后的子集划分结果:',result)
