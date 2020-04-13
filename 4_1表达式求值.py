"""
详细解析版
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
    elif theta=="^":
        return a**b
    else:  
        return a / b

if __name__=='__main__':
    OPTR=SStack()   #存运算符栈
    OPTR.push('#')
    OPND=SStack()   #存操作数栈
    string=input('请输入要计算的表达式:')   #3*(7-2)#
    for i in string:
        print('操作的符号或数字',i)
        if i.isdigit():
            i=int(i)
            print('进栈的操作数:',i)
            OPND.push(int(i))
        elif i.isdigit()==False and i!='#':
            f=Precede(OPTR.peek(),i)
            if f=='<':
                print('进栈的操作符<:',i)
                OPTR.push(i)
            elif f=='=':
                print('弹出栈的操作符=:',i)
                OPTR.pop()
            elif f=='>':
                print('f>i的操作符:',i)
                b=OPND.pop()
                a=OPND.pop()
                theta=OPTR.pop()
                print("a,b,thata:",a,b,theta)
                r1=Operate(a,theta,b)
                print('r1=',r1)
                OPND.push(r1)       
                c=OPTR.peek()
                f1=Precede(c,i)
                if f1=='<':
                    print('进栈的操作符<:',i)
                    OPTR.push(i)
                elif f1=='=':
                    OPTR.pop()
                elif f1=='>':
                    print('f1>i的操作符:',i)
                    b=OPND.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                    a=OPND.pop()
                    theta=OPTR.pop()
                    print("a,b,thata:",a,b,theta)
                    r1=Operate(a,theta,b)        
                    OPND.push(r1) 
                    f2=Precede(OPTR.peek(),i)
                    if f2=='<':
                        print('进栈的操作符<:',i)
                        OPTR.push(i)
                    elif f2=='=':
                        OPTR.pop()
                    elif f1=='>':
                        print('f2>i的操作符:',i)
                        b=OPND.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                        a=OPND.pop()
                        theta=OPTR.pop()
                        print("a,b,thata:",a,b,theta)
                        r2=Operate(a,theta,b)        
                        OPND.push(r2) 
                    
        elif i=='#':
            while OPTR.peek()!='#':
                b=OPND.pop()                #取操作数前两个元素与操作符栈顶元素进行相应运算。
                a=OPND.pop()
                theta=OPTR.pop()
                print("a,b,thata:",a,b,theta)
                r=Operate(a,theta,b)        
                OPND.push(r) 
            
            
        
                
    print('操作数栈的内容是：',OPND.content())
    print('操作符栈的内容是：',OPTR.content())
    #3+9*2-4/2#
