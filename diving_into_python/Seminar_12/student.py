# 1. Cоздайте класс студента. 
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


import csv

class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not all(map(lambda val: val.istitle(), value.split(' '))):
            raise ValueError(f"ФИО должно начинаться с заглавной буквы!")
        instance.__dict__[self.name] = value
        

class Student:
    name = NameValidator()

    def __init__(self, name):
        self.name = name
        self.subject_grades = {}
        self.subject_tests = {}

        with open('diving_into_python\Seminar_12\subjects.csv', 'r') as csv_file:
            subjects = csv.reader(csv_file, delimiter="\n")
            for item in subjects:
                self.subject_grades[item[0]] = []
                self.subject_tests[item[0]] = []
                

    def add_score(self, score, subject):
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subject_grades[subject].append(score)
    
    def add_test_result(self, result, subject):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subject_tests[subject].append(result)
    
    def average_score_student(self):
        subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        if not subject_scores:
            return 0
        return sum(subject_scores) / len(subject_scores)
    
    def subject_test_average(self, subject):
        return subject, sum(self.subject_tests[subject]) / len(self.subject_tests[subject])



# Создание экземпляра класса Student
student = Student("Иван Иванович Петров")

# Добавление оценок и результатов тестов
student.add_score(4, 'Math')
student.add_score(5, 'Math')
student.add_score(5, 'Russian')

student.add_test_result(80, 'Math')
student.add_test_result(90, 'Russian')
student.add_test_result(20, 'Russian')

# Расчет среднего балла ученика по всем предметам
print("Средний балл ученика", student.average_score_student())

# Расчет среднего балла по тестам определенного предмета 
print("Средний балл по тесту:", student.subject_test_average('Russian'))
