import matplotlib.pyplot as plt

# 假设你有6条路径的能量数据
path1 = [-100.0, -90.0, -80.0, -110.0, -100.0]
path2 = [-100.0, -85.0, -75.0, -105.0, -95.0]
path3 = [-100.0, -88.0, -78.0, -102.0, -98.0]
path4 = [-100.0, -92.0, -82.0, -108.0, -97.0]
path5 = [-100.0, -89.0, -79.0, -106.0, -96.0]
path6 = [-100.0, -91.0, -81.0, -107.0, -99.0]

# 将所有路径数据存入一个列表
paths = [path1, path2, path3, path4, path5, path6]

# 定义路径的标签
labels = ["Path 1", "Path 2", "Path 3", "Path 4", "Path 5", "Path 6"]

# 为每条路径设置不同的颜色
colors = ['b', 'r', 'g', 'm', 'c', 'y']  # 蓝色、红色、绿色、洋红、青色、黄色

# 设置横线长度（每个阶段的距离）和线之间的间距
line_length = 1
spacing = line_length * 2

# 绘制能量阶梯图
plt.figure(figsize=(12, 8))

for i, path in enumerate(paths):
    for j in range(len(path)):
        # 横线起点和终点的位置，间距设置为线长的两倍
        x_start = j * (line_length + spacing)
        x_end = x_start + line_length

        # 绘制加粗的横线
        plt.plot([x_start, x_end], [path[j], path[j]], color=colors[i], lw=4)

        # 如果不是最后一个点，绘制虚线连接
        if j < len(path) - 1:
            # 虚线从当前横线的末端到下一个横线的起始点
            plt.plot([x_end, x_end + spacing], [path[j], path[j+1]], color=colors[i], linestyle='--')

# 添加坐标轴标签
plt.xlabel('Reaction Coordinate')
plt.ylabel('Free Energy (kcal/mol)')

# 添加标题
plt.title('Reaction Energy Profile')

# 显示图例
plt.legend(labels)

# 显示图表
plt.grid(True)
plt.show()
