import matplotlib.pyplot as plt
import numpy as np
# 设置字体
plt.rcParams['font.family'] = 'SimHei'  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 定义数据
methods = ['GIN', 'GraphSage', 'Popularity', 'DCF', 'P-Companion', 'ALCIR', 'SComGNN(我们所复现的模型)']
appliances_hr5 = [0.4347, 0.4402, 0.2040, 0.3630, 0.3545, 0.3754, 0.4919]
appliances_ndcg = [0.4279, 0.4215, 0.2906, 0.3817, 0.3759, 0.3792, 0.4377]
toys_hr5 = [0.5242, 0.5313, 0.1809, 0.4876, 0.4098, 0.3930, 0.6561]
toys_ndcg = [0.4866, 0.4863, 0.2914, 0.4661, 0.3923, 0.3994, 0.5501]
grocery_hr5 = [0.4344, 0.6255, 0.2556, 0.5991, 0.4943, 0.5067, 0.7207]
grocery_ndcg = [0.4425, 0.5359, 0.3392, 0.5326, 0.4152, 0.4614, 0.5959]

# 绘制直方图
x = np.arange(len(methods))  # 方法的数量
width = 0.15  # 条形的宽度

fig, ax = plt.subplots(figsize=(12, 6))

# 绘制每个数据集的HR@5和NDCG直方图
ax.bar(x - 2*width, appliances_hr5, width, label='数据电器 的HR@5')
ax.bar(x - width, appliances_ndcg, width, label='数据电器 的NDCG')
ax.bar(x, toys_hr5, width, label='数据玩家 的 HR@5')
ax.bar(x + width, toys_ndcg, width, label='数据玩具 的NDCG')
ax.bar(x + 2*width, grocery_hr5, width, label='数据谷物 的HR@5')
ax.bar(x + 3*width, grocery_ndcg, width, label='数据谷物 的NDCG')

# 添加标签和标题
ax.set_xlabel('模型方法')
ax.set_ylabel('运行结果')
ax.set_title('比较主流模型的两个参数')
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.legend()

# 显示图表
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()