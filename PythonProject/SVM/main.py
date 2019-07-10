# -*- coding:utf-8 -*-
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors

#x横纵坐标，y分类
x = np.array([[1, 1], [4, 4], [5, 7], [6, 2], [1, 0], [1, 5], [3, 4], [5, 5], [2, 3]], dtype=int)
y = np.array([1, 0, 0, 0, 1, 1, 1, 0, 0])

# clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr')
# 非线性SCM，C越大分类效果越好，但有可能会过拟合（default C=1）。
# 高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
clf = svm.SVC(C=1, kernel='rbf', gamma=1, decision_function_shape='ovr')
clf.fit(x, y)

x1_min, x1_max = 0, 10  # 第0列的范围
x2_min, x2_max = 0, 10  # 第1列的范围
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

#设置字体
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])

# print 'grid_test = \n', grid_test
grid_hat = clf.predict(grid_test)  # 获取该区间内所有的预测值，用于画图
grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同

plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # 预测值的显示
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=cm_dark)  # 样本
plt.scatter(x[:, 0], x[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本

#图例，画图
plt.xlabel(u'维度1', fontsize=13)
plt.ylabel(u'维度2', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'SVM二特征分类', fontsize=15)
plt.grid() #网格
plt.show()
