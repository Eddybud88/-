import numpy as np


def conjugate_gradient(A, b, x0, tol=1e-10, max_iter=None):
    """
    使用共轭梯度法求解二次函数最小值问题。

    参数:
    A (np.ndarray): 正定矩阵
    b (np.ndarray): 向量
    x0 (np.ndarray): 初始点
    tol (float): 容忍误差
    max_iter (int): 最大迭代次数，默认为变量的数量

    返回:
    np.ndarray: 解向量
    int: 迭代次数
    """
    if max_iter is None:
        max_iter = A.shape[0]
    x = x0.copy().astype(np.float64)
    r = b - A @ x
    p = r.copy()
    rs_old = np.dot(r, r)

    iterations = 0
    for _ in range(max_iter):
        Ap = A @ p
        alpha = rs_old / np.dot(p, Ap)
        x += alpha * p
        r -= alpha * Ap
        rs_new = np.dot(r, r)
        iterations += 1
        if np.sqrt(rs_new) < tol:
            break
        p = r + (rs_new / rs_old) * p
        rs_old = rs_new

    return x, iterations


A = np.array([[3, 1], [1, 2]], dtype=np.float64)
b = np.array([2, 4], dtype=np.float64)

x0 = np.array([0, 0], dtype=np.float64)

solution, iterations = conjugate_gradient(A, b, x0)
print(f"Solution: {solution}")
print(f"Iterations: {iterations}")


def quadratic_function(x, A, b):
    """计算二次函数的值"""
    return 0.5 * np.dot(x, A @ x) + np.dot(b, x)


print(f"Function value at solution: {quadratic_function(solution, A, b)}")