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
            print('Нет оценок')


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
            print('Нет оценок')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
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
    print('Нет такого курса в оценках лекторов')


def average_lecturer_grade_for_one_course(lecturers, course):
    for lecturer in lecturers:
        if course in lecturer.grades:
            return round(sum((list(lecturer.grades.values())[0])) / len((list(lecturer.grades.values())[0])), 2)
    print('Нет такого курса в оценках лекторов')


student_1 = Student('Ушаков', 'Лев')
student_2 = Student('Зайцева', 'Милана')
mentor_1 = Mentor('Семенов', 'Алексей')
mentor_2 = Mentor('Савицкий', 'Константин')
lecturer_1 = Lecturer('Иванова', 'Вероника')
lecturer_2 = Lecturer('Макаров', 'Алексей')
reviewer_1 = Reviewer('Сычев', 'Федор')
reviewer_2 = Reviewer('Новикова', 'Валерия')

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

print(average_students_grade_for_one_course([student_1, student_2], 'Python'))
print(average_lecturer_grade_for_one_course([lecturer_1, lecturer_2], 'Python'))
