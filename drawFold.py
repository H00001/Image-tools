import matplotlib.pyplot as plt

max_acc_per_round = []
max_nmi_per_round = []
max_ari_per_round = []

max_f1_per_round = []



name = "ACM"
with open(f'fold/{name}.txt', 'r') as file:
    while True:
        # 读取3行
        lines = [file.readline().strip() for _ in range(3)]
        if not all(lines):
            break  # 如果读到文件末尾或者不足3行，则停止读取
        
        # 解析每一行并更新每个轮次的最大acc值
        max_acc = -float('inf')
        max_nmi = -float('inf')
        max_ari = -float('inf')
        max_f1  = -float('inf')

        for line in lines:
            parts = line.split()
            acc = float(parts[2])  # 获取acc值
            nmi = float(parts[5])  # 获取acc值
            ari = float(parts[8])  # 获取acc值
            f1 = float(parts[11])  # 获取acc值

            max_acc = max(max_acc, acc)
            max_nmi = max(max_nmi, nmi)
            max_ari = max(max_ari, ari)
            max_f1 = max(max_f1, f1)

        
        max_acc_per_round.append(max_acc)
        max_nmi_per_round.append(max_nmi)
        max_ari_per_round.append(max_ari)
        max_f1_per_round.append(max_f1)


plt.rcParams["font.family"] = "Times New Roman"
x_values = range(1, 201)
markers = ['o', 's', '^', 'd']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
marker_step = 20
plt.ylim(0,1)
plt.plot(x_values, max_acc_per_round, linewidth=2, color=colors[0],marker=markers[0], markevery=marker_step, label='ACC')
plt.plot(x_values, max_nmi_per_round, linewidth=2, color=colors[1],marker=markers[1], markevery=marker_step, label='NMI')
plt.plot(x_values, max_ari_per_round, linewidth=2, color=colors[2],marker=markers[2], markevery=marker_step, label='ARI')
plt.plot(x_values, max_f1_per_round, linewidth=2, color=colors[3],marker=markers[3], markevery=marker_step, label='F1')


plt.title(name)
plt.ylabel("Score")
plt.xlabel("Epoch")
plt.legend()


plt.savefig(f"fold/{name}.png",dpi=600)
