import numpy as np

def SOM(data, som):
    # 对于每次迭代：
    for step in range(0, 10000):
        #对于每一种模式：
        for vector in data:
            # print("对于样本: ", vector)
            # 计算欧氏距离
            distance = np.zeros([5, 5])
            for x in range(0, 5):
                for y in range(0, 5):
                    distance[x][y] = np.sum(np.square((som[x][y]-vector)))
            # print(distance)
            # 找到优胜节点
            temp = distance[0][0]
            best_x = 0
            best_y = 0
            for x in range(0, 5):
                for y in range(0, 5):
                    if distance[x][y] < temp:
                        best_x = x
                        best_y = y
                        temp = distance[x][y]
            # print(best_x, best_y)
            # 获取当前迭代次数的学习率和半径
            if step < 1000:
                study_rate = 0.5 - 0.00046 * step
                radius = 2
            else:
                study_rate = 0.04
                radius = 0
            # 对于半径内节点学习修正
            study_list = []
            if radius == 2:
                for x in range(0, 5):
                    for y in range(0, 5):
                        if(abs(x-best_x) + abs(y-best_y)) <= radius:
                            study_list.append([x, y])
                #print(study_list)
                for [a, b] in study_list:
                    som[a][b] = som[a][b] + study_rate * (vector - som[a][b])
            else:
                som[best_x][best_y] = som[best_x][best_y] + study_rate * (vector - som[best_x][best_y])
            #print(som)

        #每200观察一次
        #if step % 200 == 0:
            # print("迭代次数: ", step)
            # print("权向量是：", som)
    return  som


def SHOW(data, som):
    label = np.zeros([5, 5])
    for x in range(0, 5):
        for y in range(0, 5):
            distance = []
            for vector in data:
                distance.append(np.sum(np.square((som[x][y] - vector))))
            temp = distance[0]
            best_index = 0
            for index in range(0, 5):
                    if distance[index] < temp:
                        best_index = index
                        temp = distance[index]
            label[x][y] = best_index
    print(label)


data = np.array( [[1,0,0,0],
                  [1,1,0,0],
                  [1,1,1,0],
                  [0,1,0,0],
                  [1,1,1,1]] )

#som = np.random.rand(5, 5, 4)
som = np.zeros([5, 5, 4])
#som[0][0] = [1.1, 0, 0, 0]
SOM(data, som)
SHOW(data, som)