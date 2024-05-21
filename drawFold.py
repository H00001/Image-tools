import matplotlib.pyplot as plt

max_acc_per_round = []

name = "HHAR"
with open(f'fold/{name}.txt', 'r') as file:
    while True:
        # 读取3行
        lines = [file.readline().strip() for _ in range(3)]
        if not all(lines):
            break  # 如果读到文件末尾或者不足3行，则停止读取
        
        # 解析每一行并更新每个轮次的最大acc值
        max_acc = -float('inf')
        for line in lines:
            parts = line.split()
            acc = float(parts[2])  # 获取acc值
            max_acc = max(max_acc, acc)
        
        max_acc_per_round.append(max_acc)


plt.rcParams["font.family"] = "Times New Roman"
x_values = range(1, 201)
y_values = max_acc_per_round
            
plt.ylim(0,1)
plt.plot(x_values, y_values, linewidth=1)

plt.title(name)
plt.ylabel("Score")
plt.xlabel("Epoch")

plt.savefig(f"fold/{name}.png",dpi=600)
