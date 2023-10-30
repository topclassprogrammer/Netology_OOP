class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_student_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if isinstance(self.average_student_grade(), float) and isinstance(other.average_student_grade(), float):
            return self.average_student_grade() < other.average_student_grade()
        else:
            print('Ошибка сравнения оценок студентов')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and grade in range(11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка оценки лектора студентом')

    def average_student_grade(self):
        if self.grades:
            sum_values = 0
            for value in self.grades.values():
                sum_values += sum(value) / len(value)
            return round(sum_values, 2)
        else:
            print(f'Нет оценок у студента "{self.name} {self.surname}"')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_lecturer_grade()}')

    def __lt__(self, other):
        if isinstance(self.average_lecturer_grade(), float) and isinstance(other.average_lecturer_grade(), float):
            return self.average_lecturer_grade() < other.average_lecturer_grade()
        else:
            print('Ошибка сравнения оценок лекторов')

    def average_lecturer_grade(self):
        if self.grades:
            sum_values = 0
            for value in self.grades.values():
                sum_values += sum(value) / len(value)
            return round(sum_values, 2)
        else:
            print(f'Нет оценок у лектора "{self.name} {self.surname}"')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and grade in range(11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка оценки студента ревьюером')


def average_students_grade_for_one_course(students, course):
    for student in students:
        if course in student.grades:
            return round(sum((list(student.grades.values())[0])) / len((list(student.grades.values())[0])), 2)
    return f'Курс {course} отсутствует у студентов'


def average_lecturers_grade_for_one_course(lecturers, course):
    for lecturer in lecturers:
        if course in lecturer.grades:
            return round(sum((list(lecturer.grades.values())[0])) / len((list(lecturer.grades.values())[0])), 2)
    return f'Курс {course} отсутствует у лекторов'


student_1 = Student('Лев', 'Ушаков')
student_2 = Student('Милана', 'Зайцева')
mentor_1 = Mentor('Алексей', 'Семенов')
mentor_2 = Mentor('Константин', 'Савицкий')
lecturer_1 = Lecturer('Вероника', 'Иванова')
lecturer_2 = Lecturer('Алексей', 'Макаров')
reviewer_1 = Reviewer('Федор', 'Сычев')
reviewer_2 = Reviewer('Валерия', 'Новикова')

student_1.courses_in_progress += ['Python', 'Data Science']
student_1.finished_courses += ['HTML']
student_2.courses_in_progress += ['Data Science', 'C++', 'Python']
student_2.finished_courses += ['C#', 'Java']
lecturer_1.courses_attached += ['HTML', 'CSS', 'JavaScript', 'Python']
lecturer_2.courses_attached += ['Java', 'Data Science', 'C++', 'C#']
reviewer_1.courses_attached += ['Data Science', 'DevOps', 'SQL', 'Python']
reviewer_2.courses_attached += ['Ruby', 'Swift', 'C++', 'Python', 'Rust', 'Data Science']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Data Science', 6)
student_1.rate_lecturer(lecturer_2, 'Data Science', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Data Science', 6)
student_2.rate_lecturer(lecturer_2, 'Data Science', 8)

reviewer_1.rate_student(student_1, 'Data Science', 8)
reviewer_1.rate_student(student_1, 'Data Science', 7)
reviewer_1.rate_student(student_2, 'Python', 9)
reviewer_1.rate_student(student_2, 'Python', 8)
reviewer_2.rate_student(student_1, 'Data Science', 7)
reviewer_2.rate_student(student_1, 'Data Science', 10)
reviewer_2.rate_student(student_2, 'Python', 9)
reviewer_2.rate_student(student_2, 'Python', 7)

print(f'Студент 1:\n{student_1}\n', end=f'{"-" * 50}\n')
print(f'Студент 2:\n{student_2}\n', end=f'{"-" * 50}\n')
print(f'Лектор 1:\n{lecturer_1}\n', end=f'{"-" * 50}\n')
print(f'Лектор 2:\n{lecturer_2}\n', end=f'{"-" * 50}\n')
print(f'Ревьюер 1:\n{reviewer_1}\n', end=f'{"-" * 50}\n')
print(f'Ревьюер 2:\n{reviewer_2}\n', end=f'{"-" * 50}\n')

if student_1 < student_2:
    print(f'У студента {student_1.name} {student_1.surname} средняя оценка по домашним заданиям меньше, '
          f'чем у студента {student_2.name} {student_2.surname}')
elif student_1 > student_2:
    print(f'У студента {student_1.name} {student_1.surname} средняя оценка по домашним заданиям больше, '
          f'чем у студента {student_2.name} {student_2.surname}')
else:
    print(f'У студентов {student_1.name} {student_1.surname} и {student_2.name} {student_2.surname} '
          f'средние оценки по домашним заданиям одинаковы')

if lecturer_1 < lecturer_2:
    print(f'У лектора {lecturer_1.name} {lecturer_1.surname} средняя оценка за лекции меньше, '
          f'чем у лектора {lecturer_2.name} {lecturer_2.surname}')
elif lecturer_1 > lecturer_2:
    print(f'У лектора {lecturer_1.name} {lecturer_1.surname} средняя оценка за лекции больше, '
          f'чем у лектора {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'У студентов {lecturer_1.name} {lecturer_1.surname} и {lecturer_2.name} {lecturer_2.surname} '
          f'средние оценки за лекции одинаковы')

print(f'Средняя оценка по домашним заданиям по всем студентам в рамках курса: '
      f'{average_students_grade_for_one_course([student_1, student_2], "Python")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса: '
      f'{average_lecturers_grade_for_one_course([lecturer_1, lecturer_2], "Data Science")}')
