def record_person_info(name, student_id, major, *hobbies, **other_info):
    """
    记录个人信息。

    参数:
    name (str): 姓名
    student_id (str): 学号
    major (str): 专业
    hobbies (tuple): 爱好列表
    other_info (dict): 其他信息，如年龄、邮箱等

    返回:
    dict: 包含个人信息的字典
    """
    person_info = {
        'name': name,
        'student_id': student_id,
        'major': major,
        'hobbies': hobbies,
    }
    person_info.update(other_info)

    return person_info


info = record_person_info(
    name="zyx",
    student_id="U202110071",
    major="统计学",
    hobbies=("阅读", "看电影"),
    age=21,
    email="823123514@qq.com"
)

print(info)