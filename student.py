
class student:

    def __init__(self, name=None, id=None, major=None, gpa=None):
        self.name = name
        self.id = id
        self.major = major
        self.gpa = gpa

    def display_info(self):
        print("имя:", self.name)
        print("айди:", self.id)
        print("специальность:", self.major)
        print("средний балл:", self.gpa)

    def study(self):
        print(self.name, "учится")


students = []

number = int(input("количество студентов: "))

for i in range(number):
    print("\nстудент", i + 1)

    choice = input("1 - по умолчанию, 2 - с параметрами: ")

    if choice == "1":
        student1 = student()
    else:
        name = input("имя: ")
        id = input("айди: ")
        major = input("специальность: ")
        gpa = float(input("средний балл: "))

        student1 = student(name, id, major, gpa)

    students.append(student1)


print("\nинформация о студентах:")

for student1 in students:
    student1.display_info()
    student1.study()
    print()
