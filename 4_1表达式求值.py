"""
表达式求值问题
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
    #输出栈内容
    def content(self):
        #print (self.items)
        return self.items
    #把新的元素堆进栈里
    def push(self,data):
        return self.items.append(data)
    #把栈顶元素弹出
    def pop(self):
        return self.items.pop()
def Precede(f1,f2):
    """
    Compare the prior of operator f1 and f2
    """
    # the prior of operator
    prior = (
        #列为表达式右边，行为表达式左边
         #   '+'  '-'  '*'  '/'  '('  ')'  '^'  '#'
            ('>', '>', '<', '<', '<', '>', '<', '>'), # '+'
            ('>', '>', '<', '<', '<', '>', '<', '>'), # '-'
            ('>', '>', '>', '>', '<', '>', '<', '>'), # '*'
            ('>', '>', '>', '>', '<', '>', '<', '>'), # '/'
            ('<', '<', '<', '<', '<', '=', '<', ' '), # '('
            ('>', '>', '>', '>', ' ', '>', '>', '>'), # ')'
            ('>', '>', '>', '>', '<', '>', '>', '>'), # '^'
            ('<', '<', '<', '<', '<', ' ', '<', '=')  # '#'   
         )
    # operator to index of prior[8][8]
    char2num = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '(': 4,
        ')': 5,
        '^': 6,
        '#': 7
    }
    return prior[char2num[f1]][char2num[f2]]

##定义基本操作函数
def Operate(a,theta,b):
    """
    根据运算符号operator计算结果并返回
    """
    if theta == "+":
        return a + b
    elif theta == "-":
        return a - b
    elif theta == "*":
        return a * b
    else:  
        return a / b
#定义求值函数
def calculate(string,stack1,stack2):            #stack1为操作数栈的形参  stack2为操作符的形参
    for i in string:
        if i.isdigit():
            i=int(i)
            stack1.push(int(i))                #将数字压入操作数栈。
        elif i.isdigit()==False and i!='#':
            f=Precede(stack2.peek(),i)
            if f=='<':
                stack2.push(i)                 #新遍历的操作符优先级比操作符栈顶元素高，将其压入操作符栈。
            elif f=='=':
                stack2.pop()                   #新遍历的操作符优先级与操作符栈顶元素相等，去除操作符栈顶元素。
            elif f=='>':                      #新遍历的操作符优先级与操作符栈顶元素低，，，，
                b=stack1.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                a=stack1.pop()
                theta=stack2.pop()
                r1=Operate(a,theta,b)        
                stack1.push(r1)               #将得到的结果值压入操作数栈。
                c=stack2.peek()               
                f1=Precede(c,i)              #继续将该新遍历的操作符与当前操作符栈顶元素比较优先级
                if f1=='<':
                    stack2.push(i)
                elif f1=='=':
                    stack2.pop()
                elif f1=='>':
                    b=stack1.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                    a=stack1.pop()
                    theta=stack2.pop()
                    r1=Operate(a,theta,b)        
                    stack1.push(r1) 
                    f2=Precede(OPTR.peek(),i)              #继续将该新遍历的操作符与当前操作符栈顶元素比较优先级
                    if f2=='<':
                        stack2.push(i)
                    elif f2=='=':
                        stack2.pop()
                    elif f2=='>':
                        b=stack1.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                        a=stack1.pop()
                        theta=stack2.pop()
                        r2=Operate(a,theta,b)        
                        stack1.push(r2) 
        elif i=='#':
            while stack2.peek()!='#':
                b=stack1.pop()
                a=stack1.pop()
                theta=stack2.pop()
                r=Operate(a,theta,b)
                stack1.push(r)
            return r

if __name__=='__main__':
    OPTR=SStack()   #存运算符栈
    OPTR.push('#')
    OPND=SStack()   #存操作数栈
    string=input('请输入要计算的表达式,一定要以"#"结尾：\n')   #3*(7-2)#   3+9*2-4/2#
    result=calculate(string,OPND,OPTR)
    print('最终计算结果为：',result)
    print('最终操作数栈的结果：',OPND.content())
