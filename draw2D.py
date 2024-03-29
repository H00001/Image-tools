#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 数据
NAME = "HHAR"

if NAME == "CITE":
    sta = 0.0
    end = 0.8

if NAME == "ACM":
    sta = .3
    end = 1

if NAME == "HHAR":
    sta = 0.3
    end = 1
if NAME == "REUT":
    sta = 0.1
    end = 1
if NAME == "USPS":
    sta = 0.3
    end = 0.9

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

categories = ['ACC', 'NMI', 'ARI', 'F1']
group_names = ['BASE', '-F', '-C', 'OURS']

colors = ['#010080', '#2368A3', '#3172CC', '#C5D9FA']

values_ACM = np.array(
    [
        [0.7808, 0.4619, 0.4938, 0.7683],
        [0.9220, 0.7254, 0.7814, 0.9227],
        [0.8691, 0.6028, 0.6489, 0.8673],
        [0.9372, 0.7654, 0.8220, 0.9374],
    ]
)

values_CITE = np.array(
    [[0.3835, 0.1309, 0.1176, 0.3626],
     [0.7084, 0.4404, 0.4655, 0.6178],
     [0.7078, 0.4432, 0.4673, 0.6241],
     [0.7259, 0.4580, 0.4831, 0.6455]]
)

values_HHAR = np.array(
    [[0.5710, 0.6121, 0.4501, 0.5326],
     [0.8476, 0.7591, 0.7079, 0.8466],
     [0.7300, 0.7131, 0.6114, 0.7169],
     [0.8815, 0.8442, 0.7838, 0.8863],
     ]
)

values_REUT = np.array(
    [[0.4863, 0.1548, 0.1373, 0.3725],
     [0.7967, 0.5605, 0.5899, 0.7580],
     [0.5496, 0.3327, 0.2155, 0.5349],
     [0.8382, 0.6299, 0.6793, 0.7945]
    ]
)

values_USPS = np.array(
    [[0.6311, 0.5510, 0.4573, 0.5969],
     [0.7944, 0.8207, 0.7535, 0.7819],
     [0.7937, 0.7910, 0.7646, 0.7051],
     [0.8096, 0.8275, 0.7646, 0.7925],
     ]
)

# values = np.roll(values, shift=-1, axis=1)
# values[:, [0, 3]] = values[:, [3, 0]]

# 绘制条状图
bar_width = 0.2  # 条带宽度
gap_width = 0.01  # 间隙宽度
for i, group_name in enumerate(group_names):
    positions = np.arange(len(categories)) + (bar_width + gap_width) * i
    plt.bar(positions, eval(f"values_{NAME}")[i], bar_width, label=group_name, color=colors[i])

# 添加标题和标签
plt.title("")
plt.xlabel(NAME, fontweight='bold', fontsize='18')
plt.ylabel('Score', fontweight='bold', fontsize='18')
plt.ylim(sta, end)

plt.xticks(np.arange(len(categories)) + bar_width * 1.5, categories)  # 设置x轴刻度位置
legend = plt.legend(ncol=4, fontsize="13", frameon=False, loc='upper center')

plt.savefig(f'{NAME}_abolish.png', dpi=600)
# 显示图形
plt.show(dpi=600)
