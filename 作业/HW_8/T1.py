import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

np.random.seed(0)

x = np.linspace(-20, 20, 1000)

# 参数
means = [0]  # 均值
std_devs = [1, 2, 5, 10]  # 标准差

# 绘制不同σ的正态分布曲线
plt.figure(figsize=(12, 6))

for std_dev in std_devs:
    y = norm.pdf(x, loc=means[0], scale=std_dev)
    plt.plot(x, y, label=f'σ={std_dev}')

plt.title('正态分布曲线（μ=0）')
plt.xlabel('x')
plt.ylabel('概率密度')
plt.legend()
plt.grid(True)

# 生成1000个随机数，μ=0，σ=2
mu, sigma = 0, 2
random_numbers = np.random.normal(mu, sigma, 1000)

# 绘制频率分布直方图和正态分布曲线
plt.figure(figsize=(12, 6))

# 频率分布直方图
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g', edgecolor='black', label='随机数直方图')

# 正态分布曲线
xmin, xmax = plt.xlim()
x_hist = np.linspace(xmin, xmax, 100)
p = norm.pdf(x_hist, mu, sigma)
plt.plot(x_hist, p, 'k', linewidth=2, label='正态分布曲线')

plt.title('频率分布直方图与正态分布曲线（μ=0, σ=2）')
plt.xlabel('x')
plt.ylabel('密度')
plt.legend()
plt.grid(True)

plt.show()
