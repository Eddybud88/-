class Student:
    def __init__(self, name: str, age: int, score: dict):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_course(self) -> int:
        return max(self.score.values())

if __name__ == "__main__":
    student_example = Student("zyx", 21, {"运筹学": 95, "多元统计": 88, "体育": 90})
    name = student_example.get_name()
    age = student_example.get_age()
    highest_score = student_example.get_course()
    print(name, age, highest_score)
