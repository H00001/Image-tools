import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取Excel文件
data = pd.read_excel('DATA.xlsx', sheet_name=-1)  # 读取最后一个工作表

plt.rcParams['font.sans-serif'] = ['Times New Roman']
# 画布
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 数据
xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))  # 网格
xpos = xpos.flatten()   # 将网格展平
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.85
dz = data.values.flatten()

# 绘制3D条形图
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

# 设置坐标轴标签
ax.set_xticks(np.arange(data.shape[1]))  # 设置刻度位置
ax.set_xticklabels(['5', '4', '3', '2', '1'])
ax.set_yticks(np.arange(data.shape[0]))
ax.set_yticklabels(['0.01', '0.1', '1', '10', '100'])
ax.set_xlabel('K')
ax.set_ylabel('r_a')
ax.set_zlabel('Accuracy(%)')

# 设置Z轴限制
ax.set_zlim(0, 70)

plt.show()