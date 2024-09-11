import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

a = 1

theta = np.linspace(0, 2 * np.pi, 1000)

r = a * (1 - np.sin(theta))

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, label='Cardioid (r = 1 - sin(θ))')

ax.set_title('笛卡尔心形图', va='bottom')
ax.set_rlabel_position(-22.5)

ax.legend()

plt.show()
