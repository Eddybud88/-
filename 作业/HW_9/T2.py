import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置随机种子
np.random.seed(1234)

# 创建DataFrame
df = pd.DataFrame(np.random.randn(10, 4), columns=['Col1', 'Col2', 'Col3', 'Col4'])

# 添加分组列
df['Group'] = pd.Series(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])
df['SubGroup'] = pd.Series(['X', 'X', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'Y'])

# 1: 基本箱线图
plt.figure(figsize=(10, 6))
df.boxplot()
plt.title('基本箱线图')
plt.grid(True)
plt.show()

# 2: 按列分组的箱线图
plt.figure(figsize=(10, 6))
df.boxplot(by='Group', grid=True)
plt.title('按列分组的箱线图')
plt.xlabel('组')
plt.ylabel('值')
plt.grid(True)
plt.subplots_adjust(top=0.85)
plt.show()

# 3: 按多个列分组的箱线图
plt.figure(figsize=(12, 8))
df.boxplot(column=['Col1', 'Col2'], by=['Group', 'SubGroup'], grid=True, layout=(2, 1))
plt.suptitle('按多个列分组的箱线图')
plt.xlabel('组和子组')
plt.ylabel('值')
plt.grid(True)
plt.subplots_adjust(top=0.85)
plt.show()

# 4: 调整字体大小和旋转标签的箱线图
plt.figure(figsize=(10, 6))
df.boxplot(grid=False, rot=45, fontsize=12)
plt.title('调整字体大小和旋转标签的箱线图')
plt.xlabel('列')
plt.ylabel('值')
plt.grid(True)
plt.show()

# 5: 返回不同类型的结果
# 返回 'dict' 类型
boxplot_dict = df.boxplot(return_type='dict')
print("返回的字典类型结果:")
print(boxplot_dict)

# 返回 'axes' 类型
boxplot_axes = df.boxplot(return_type='axes')
print("返回的 axes 类型结果:")
print(type(boxplot_axes))