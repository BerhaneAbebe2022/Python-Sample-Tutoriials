class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade    # grade 0 - 100

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):

        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return "The course is already full, we can not register you."

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)

if __name__=="__main__":
    course = Course("Science", 4)
    s1 = Student("Tim", 19, 95)
    s2 = Student("Aron", 19, 65)
    s3 = Student("Hana", 19, 75)
    s4 = Student("Azu", 18, 85)
    s5 = Student("Titi", 20, 80)
    course.add_student(s1)
    course.add_student(s2)
    course.add_student(s3)
    course.add_student(s4)
    course.get_average_grade()
    course.add_student(s5)


        
