class Student:
  def __int__(self, student_id, name, marks, age)
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
  def __init__(self)
    students = []


  def add_student(self):
     student_id = int(input("Enter Student ID: "))

    for student in students:
      if student.student_id == student_id: 
        print("Student already exist")

    name = input("Enter the Name of Student:- ")
    marks = float(input("Enter Marks of Student:- "))
    age = int(input("Enter the Age of Student:- "))

    new_student = Student(student_id , name , marks, age)
    students.append(new_student)
    print("Student added succesfully")



  def view_students(self):
    if not students:
      print("No student record found")


    print("\n----Student Record-----")
    for student in students:
      student.display()


  def search_student(self):
    search_id = int(input("Enter Students Id to search"))

    for student in students:
      if student.student_id = search_id:
        print("Student found")
        student.display()
      else:
        print("No Student Found")

  def  delete_student(self):
    student_id = int(input("Enter Student Id to delete:- "))

    for student in students:
      if student.student_id = student_id:
        students.remove(student)
        print("Student removed")
      else:
        print("Student not found")

  def update_marks(self):
    student_id = int(input("Enter Student Id to delete:- "))

    for student in students:
      if student.student_id = student_id:
        new_marks = float(input("Enter new marks:- "))
        student.marks = new_marks
        print("Marks Updated")
      else:
        print("Student not found")

  def highest_marks_student(self):
    if not students:
      print("No Student record found")

    topper = students[0]
    for student in students:
      if student.marks > topper.marks:
        topper = student
    print("\n---- Topper ----")
    topper.display()



def main():
  shaurya = StudentManagementSystem()

  while True:
    print("\n---- STUDENT MANAGEMENT SYSTEM ----")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Highest Marks Student")
    print("7. Exit")

    choice = int(input("Enter Choice:- ")


    if choice == "1":
      shaurya.add_student()

    elif choice == "2"::
      shaurya.view_student() 

    elif choice == "3":
      shaurya.search_student()

    elif choice == "4":
      shaurya.update_marks()

    elif choice == "5":
      shaurya.delete_student()

    elif choice == "6"
      shaurya.highest_marks_student()

    elif choice == "7":
      print("Exiting the program....")
      break

    else:
      print("Invalid Choice")

main()
