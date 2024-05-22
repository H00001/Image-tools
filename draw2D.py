#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 数据
NAME = "ACM"

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

if NAME == "DBLP":
    sta = 0.0
    end = 0.9

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

categories = ['ACC', 'NMI', 'ARI', 'F1']
group_names = ['BASE', '-S', '-F', 'OURS']

colors = ['#F5834A', '#FEAB43', '#FBD54A', '#ECEE66']

values_ACM = np.array(
    [
        [0.7808, 0.4619, 0.4938, 0.7683],
        [0.9020, 0.6954, 0.7414, 0.8727],
        [0.8691, 0.6028, 0.6489, 0.8673],
        [0.9140, 0.7073, 0.7629, 0.8876],
    ]
)

values_CITE = np.array(
    [[0.3835, 0.1309, 0.1176, 0.3626],
     [0.6584, 0.4404, 0.4655, 0.6178],
     [0.6678, 0.3663, 0.4673, 0.6241],
     [0.6793, 0.4200, 0.4831, 0.6455]]
)

values_HHAR = np.array(
    [[0.5710, 0.6121, 0.4501, 0.5326],
     [0.8476, 0.7591, 0.7079, 0.8466],
     [0.7300, 0.7131, 0.6114, 0.7169],
     [0.8843, 0.8248, 0.7629, 0.8836],
     ]
)

values_REUT = np.array(
    [[0.4863, 0.1548, 0.1373, 0.3725],
     [0.7867, 0.5605, 0.5899, 0.7580],
     [0.5496, 0.3327, 0.2155, 0.5349],
     [0.8023, 0.5700, 0.5700, 0.7888]
    ]
)

values_USPS = np.array(
    [[0.6311, 0.5510, 0.4573, 0.5969],
     [0.7944, 0.8207, 0.7535, 0.7819],
     [0.7937, 0.7910, 0.7646, 0.7051],
     [0.8096, 0.8275, 0.7646, 0.7925],
     ]
)

values_DBLP = np.array(
    [[0.6311, 0.3410, 0.3873, 0.5969],
     [0.6744, 0.3407, 0.35, 0.6819],
     [0.6737, 0.3210, 0.3646, 0.6951],
     [0.7000, 0.3600, 0.3900, 0.7085]]
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

plt.savefig(f'abolish/{NAME}_abolish.png', dpi=600)
# 显示图形
#plt.show()
