
class ListNode(object):
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
# 创建链表类
class CreateLinkList(object):
    def __init__(self): 
        self.head = ListNode(None)
    # 链表初始化函数，将data的值输入到链表中
    def InitList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return self.head
    # 链表判空
    def IsEmpty(self):
        p = self.head
        if p.next == None:
            print("Empty List!")
            return 1
        else:
            return 0

    # 计算链表长度
    def GetLength(self):
        if self.IsEmpty():
            return 0
        p = self.head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    # 遍历链表，输出链表的每个结点值，用“,”隔开
    def ReadList(self):
        if self.IsEmpty():
            return 0
        p = self.head
        while p:
            print(p.data,end = '-->')
            p = p.next
        print('')

    # 获取链表第i个结点数据
    def UpdateList(self, i,num):
        if i > self.GetLength():
            print("第%d个元素不存在", i)
            return 0
        p = self.head
        index = 1
        while index < i:
            p = p.next
            index += 1
        p.data=num
        return p.data

    # 链表插入数据，在第i个结点后插入数据data
    def InsertList(self, i, data):
        if i > self.GetLength():
            print("插入失败！")
            exit(0)
        p = self.head
        index = 1
        while index < i-1:
            p = p.next
            index += 1

        node = ListNode(data)
        node.next = p.next
        p.next = node

    # 链表删除函数，删除第i个结点
    def DeleteList(self, i):
        if i > self.GetLength():
            print("删除失败！")
            exit(0)
        index = 1
        p = self.head
        while index < i:
            pre = p
            index += 1
            p = p.next
        pre.next = p.next
        p = None

if __name__ == '__main__':
    l1 = CreateLinkList()
    print('创建单链表状态:',l1.ReadList())
    # 链表数据
    data=input('请输入单链表的结点数据，以,号隔开:').split(',')
    data=[int(i) for i in data]
    #data=[1,2,3,4,5]
    l1.InitList(data)
    print('初始化单链表:')
    l1.ReadList()
    # 读取链表的第4个结点值
    #print('单链表第4个结点值:',list.GetList(4))
    # 在第i个结点后插入一个结点
    pos=int(input('请输入插入结点位置:'))
    num=int(input('请输入插入结点元素:'))
    l1.InsertList(pos, num)
    print('插入元素后单链表:')
    l1.ReadList()
    # 删除第i个结点
    pos1=int(input('请输入删除结点位置:'))
    l1.DeleteList(pos1)
    print('删除元素后单链表:')
    l1.ReadList()
    pos2=int(input('请输入更新结点位置:'))
    num1=int(input('请输入更新结点元素:'))
    l1.UpdateList(pos2,num1)
    print('更新元素后单链表:')
    l1.ReadList()
    print('单链表长度:',l1.GetLength())
