import itertools

def sigma_algebra(omega, sets):
    def format_set(s, omega):
        if not s:
            return "∅"
        elif s == omega:
            return "Ω"
        else:
            return "{" + ", ".join(map(str, sorted(s))) + "}"

    # 初始化σ代数
    sigma = {frozenset(), frozenset(omega)}

    # 迭代添加集合及其补集
    for s in sets:
        sigma.add(frozenset(s))
        sigma.add(frozenset(omega) - frozenset(s))

    # 迭代添加并集
    while True:
        new_sets = set()
        for a, b in itertools.combinations(sigma, 2):
            new_sets.add(a | b)
        if new_sets.issubset(sigma):
            break
        sigma.update(new_sets)

    # 返回格式化后的集合列表
    return [format_set(s, omega) for s in sigma]

# 样本空间
omega = {1, 2, 3, 4, 5, 6}

# 问题 1：生成包含 {1} 的最小σ代数
sets_1 = [{1}]
formatted_sigma_1 = sigma_algebra(omega, sets_1)

# 问题 2：生成包含 {1} 和 {2} 的最小σ代数
sets_2 = [{1}, {2}]
formatted_sigma_2 = sigma_algebra(omega, sets_2)

# 输出结果
print("包含 {1} 的最小σ代数:")
print(formatted_sigma_1)

print("\n包含 {1} 和 {2} 的最小σ代数:")
print(formatted_sigma_2)


