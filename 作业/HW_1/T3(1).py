def judge_rank(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'E'

grade = float(input("请输入分数："))
rank = judge_rank(grade)
print(f"分数为{grade}，等级为：{rank}")
