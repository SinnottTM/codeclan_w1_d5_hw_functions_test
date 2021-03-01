class Student:
    def __init__(self, student_name, student_cohort):
        self.name = student_name
        self.cohort = student_cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, choice):
        return "I love " + choice

    # 