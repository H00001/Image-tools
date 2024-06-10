import matplotlib.pyplot as plt
import numpy as np

# 数据
NAME = "HHAR"

# 根据不同的NAME设置不同的y轴范围
if NAME == "CITE":
    sta = 0.0
    end = 0.8
elif NAME == "ACM":
    sta = 0.3
    end = 1
elif NAME == "HHAR":
    sta = 0.3
    end = 1
elif NAME == "REUT":
    sta = 0.1
    end = 1
elif NAME == "USPS":
    sta = 0.3
    end = 0.9
elif NAME == "DBLP":
    sta = 0.0
    end = 0.9

# 设置图表字体和样式
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

# 定义类别和组名
categories = ['ACC', 'NMI', 'ARI', 'F1']
group_names = ['BASE', '-A', '-B', '-AB']

# 定义颜色
colors = ['#f5c2b1', '#f09971', '#de752d', '#ba6124']

# 定义不同数据集的值
values_ACM = np.array(
    [
        [0.7808, 0.4619, 0.4938, 0.7683],
        [0.9020, 0.6954, 0.7414, 0.8727],
        [0.8891, 0.6828, 0.7289, 0.8673],
        [0.9180, 0.7173, 0.7729, 0.9196],
    ]
)


values_CITE = np.array(
    [[0.3835, 0.1309, 0.1176, 0.3626],
     [0.6584, 0.4204, 0.4655, 0.6178],
     [0.6678, 0.3863, 0.4673, 0.6241],
     [0.7002, 0.4301, 0.4398, 0.6572]]
)

values_HHAR = np.array(
    [[0.5710, 0.6121, 0.4501, 0.5326],
     [0.8476, 0.7591, 0.7079, 0.8436],
     [0.8520, 0.7631, 0.7114, 0.8569],
     [0.8855, 0.8348, 0.7839, 0.8900],
     ]
)

values_REUT = np.array(
    [[0.4863, 0.1548, 0.1373, 0.3725],
     [0.7867, 0.5605, 0.5899, 0.7580],
     [0.7596, 0.5327, 0.5755, 0.7431],
     [0.8023, 0.6000, 0.6164, 0.7882]
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
     [0.6944, 0.3407, 0.35, 0.6819],
     [0.6837, 0.3210, 0.3646, 0.6951],
     [0.7306, 0.4036, 0.4233, 0.7295]]
)
# ... 其他数据集的值

# 选择当前数据集的值
values = eval(f"values_{NAME}")

# 绘制条状图
bar_width = 0.1  # 条带宽度
gap_width = 0.05  # 间隙宽度
for i, group_name in enumerate(group_names):
    positions = np.arange(len(categories)) + (bar_width + gap_width) * i
    plt.barh(positions, values[i], bar_width, label=group_name, color=colors[i])

# plt.axis('off')

plt.axis('tight')
# 添加标题和标签
plt.title("")
plt.xlabel('Score', fontweight='bold', fontsize='18')
plt.ylabel(NAME, fontweight='bold', fontsize='18')
plt.xlim(sta, end)  # 注意这里改为了xlim，因为现在是横向的条形图

plt.yticks(np.arange(len(categories)) + bar_width * 1.5, categories)  # 设置y轴刻度位置
legend = plt.legend(ncol=1, fontsize="13", frameon=False, loc='center right', bbox_to_anchor=(1, .5))

plt.grid(axis='x', linestyle='--', alpha=0.7)



# 保存图形
plt.savefig(f'abolish/{NAME}_abolish.png', dpi=600)

# 显示图形
#plt.show()
