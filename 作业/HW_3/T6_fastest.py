import numpy as np


def gradient_descent(A, b, x0, learning_rate, tol=1e-5, max_iter=1000):
    """
    使用最速下降法求解二次函数最小值问题。

    参数:
    A (np.ndarray): 正定矩阵
    b (np.ndarray): 向量
    x0 (np.ndarray): 初始点
    learning_rate (float): 学习率
    tol (float): 容忍误差
    max_iter (int): 最大迭代次数

    返回:
    np.ndarray: 解向量
    """
    x = x0.astype(np.float64).copy()
    grad = A @ x + b  
    for _ in range(max_iter):
        if np.linalg.norm(grad) < tol:
            break
        x -= learning_rate * grad
        grad = A @ x + b
    return x


A = np.array([[2, 1], [1, 2]], dtype=np.float64)
b = np.array([1, 1], dtype=np.float64)
x0 = np.array([0, 0], dtype=np.float64)
learning_rate = 0.01

solution = gradient_descent(A, b, x0, learning_rate)
print(solution)