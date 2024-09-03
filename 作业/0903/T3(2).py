def calculate_gpa(score):
    try:
        score = float(score)
        if 90 <= score <= 100:
            return 4.0
        elif 80 <= score <= 89:
            return 3.0
        elif 70 <= score <= 79:
            return 2.0
        elif 60 <= score <= 69:
            return 1.0
        elif 0 <= score <= 59:
            return 0
        else:
            return -1
    except ValueError:
        return None

try:
    score_input = input("请输入成绩：")
    gpa = calculate_gpa(score_input)
    if gpa == -1:
        print("请输入范围内的正确成绩")
    elif gpa is not None:
        print(f"成绩为{score_input}，对应的GPA是：{gpa}")
    else:
        print("输入不是数字，请输入一个有效的数字成绩")
except Exception as e:
    print(f"发生错误：{e}")
