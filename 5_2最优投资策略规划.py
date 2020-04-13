def investment_strategy(R,F1,F2):
    Position = np.mat(np.identity(R.shape[0]))##shape[0]为随机矩阵的行数
    optimal_path = []     #新建空列表，存放每年选择的最优投资种类
    revenue_changes = []  #新建空列表，存放每年结算的最优收益
    
    #第一年进行投资
    optimal_revenue= max(Position.dot(R[:,0]))  #找出第一年各种投资中收益最大的一个
    optimal_path.append(np.argmax(Position.dot(R[:,0])))#argmax返回的是最大数的索引，放入路径中
    revenue_changes.append(optimal_revenue.item())
    
    #后续9年的投资情况
    for j in range(1, R.shape[1]):  #R.shape[1]表示R矩阵的列数，代表年，一共10年
        #分别计算转移投资和不转移投资的收益率情况，y1、y2
        y1 = (max(Position.dot(R[:, j])) - F2)
        y2 = (Position[optimal_path[j - 1]].dot(R[:, j]) - F1)
        if y1 >= y2:   #转移投资收益更大
            optimal_path.append(np.argmax(Position.dot(R[:, j])))
            optimal_revenue = optimal_revenue * (max(Position.dot(R[:, j])) - F2)
            revenue_changes.append(optimal_revenue.item())
        else:   #不转移投资收益更大
            pass
            optimal_path.append(np.argmax(optimal_path[j - 1]))
#             print('哈哈哈',optimal_path)
            optimal_revenue = optimal_revenue * (Position[optimal_path[j - 1]].dot(R[:, j]) - F1)
            revenue_changes.append(optimal_revenue.item())
    return optimal_path,revenue_changes,optimal_revenue.item()

if __name__=='__main__':
    import numpy as np
    ###建立一个具有标准正态分布的8种*10年的随机混淆矩阵——收益矩阵;行代表投资种类，列代表年份
    R=np.mat(1.1+np.random.randn(8,10)*0.1)     
    F1,F2=0.01,0.02
    optimal_path,revenue_changes,max_revenue=investment_strategy(R,F1,F2) #调用最优投资策略函数，并获取返回值
    print('投资收益矩阵：\n',R)
    print('10年最优投资策略: ',optimal_path)
    print('累计最优投资收益: ',revenue_changes)
    print('最终最优收益: ',max_revenue)
