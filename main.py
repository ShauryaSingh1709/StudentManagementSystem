class Student:
    def __init__(self, student_id, name, marks, age):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.age = age

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.student_id == student_id:
                print("Student already exists")
                return

        name = input("Enter Name of Student: ")
        marks = float(input("Enter Marks of Student: "))
        age = int(input("Enter Age of Student: "))

        new_student = Student(student_id, name, marks, age)
        self.students.append(new_student)

        print("Student added successfully")

    def view_students(self):
        if not self.students:
            print("No student records found")
            return

        print("\n----- STUDENT RECORDS -----")

        for student in self.students:
            student.display()
            print("-------------------------")

    def search_student(self):
        search_id = int(input("Enter Student ID to search: "))

        for student in self.students:
            if student.student_id == search_id:
                print("Student Found")
                student.display()
                return

        print("No Student Found")

    def delete_student(self):
        student_id = int(input("Enter Student ID to delete: "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Removed")
                return

        print("Student Not Found")

    def update_marks(self):
        student_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter New Marks: "))
                student.marks = new_marks
                print("Marks Updated")
                return

        print("Student Not Found")

    def highest_marks_student(self):
        if not self.students:
            print("No Student Records Found")
            return

        topper = self.students[0]

        for student in self.students:
            if student.marks > topper.marks:
                topper = student

        print("\n----- TOPPER -----")
        topper.display()


def main():
    shaurya = StudentManagementSystem()

    while True:
        print("\n----- STUDENT MANAGEMENT SYSTEM -----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Highest Marks Student")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            shaurya.add_student()

        elif choice == "2":
            shaurya.view_students()

        elif choice == "3":
            shaurya.search_student()

        elif choice == "4":
            shaurya.update_marks()

        elif choice == "5":
            shaurya.delete_student()

        elif choice == "6":
            shaurya.highest_marks_student()

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
