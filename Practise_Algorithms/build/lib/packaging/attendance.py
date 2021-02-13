class Student:
    name = None
    department = None
    roll_no = None
    attendance = None

    def __init__(self, name, department, roll_no, attendance=0):
        self.name = name
        self.department = department
        self.roll_no = roll_no
        self.attendance = attendance

    def update_attendance(self):
        self.attendance += 1


class Attendance():
    classes = 50

    def __init__(self):
        self.debarred_list = []

    def diplay_low_attendance(self, *student_list):
        for student in student_list:
            if student.attendance / self.classes < 0.75:
                self.debarred_list.append(student.roll_no)

        print("The roll numbers of the debarred students are-")
        print(self.debarred_list)


def main():
    student1 = Student("student1", "CSE", 1, 21)
    student2 = Student("student2", "Mech", 2, 27)
    student3 = Student("student3", "CSE", 3, 77)
    student4 = Student("student4", "EEE", 4, 45)
    student5 = Student("student5", "CSE", 5, 23)

    student6 = Student("student6", "ME", 6, 39)
    student7 = Student("student7", "ME", 7, 20)
    student8 = Student("student8", "ME", 8, 45)

    student1.update_attendance()
    student2.update_attendance()
    student3.update_attendance()
    student4.update_attendance()
    student5.update_attendance()
    student1.update_attendance()
    student2.update_attendance()
    student3.update_attendance()

    Attendance().diplay_low_attendance(
        student1,
        student2,
        student3,
        student4,
        student5)

    Attendance().diplay_low_attendance(
        student1,
        student2,
        student3)


if __name__ == '__main__':
    main()
