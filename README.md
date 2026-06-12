# Student Management System

A modern, interactive **Student Record Management System** built with Python's Object-Oriented Programming paradigm.

![Python](https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python)
![OOP](https://img.shields.io/badge/OOP-Concept-success?style=for-the-badge)

##  Overview

This project demonstrates practical application of OOP concepts to manage student records through a command-line interface. Built from scratch to help understand real-world programming patterns.

## Features

| Feature | Description |
|---------|-------------|
| Add Student | Register new students with unique IDs |
| View All Students | Display complete student database |
| Search Student | Find student records by ID |
| Update Marks | Modify student marks |
| Delete Student | Remove student records |
| Top Performer | Identify student with highest marks |
| Exit | Clean application termination |

## Project Structure

```
main.py
├── Student Class
│   ├── student_id
│   ├── name
│   ├── age
│   └── marks
└── StudentManagementSystem Class
    ├── add_student()
    ├── view_students()
    ├── search_student()
    ├── update_marks()
    ├── delete_student()
    └── highest_marks_student()
```

##  Tech Stack

- **Python ** 
- **OOP Principles** 

##  Code Walkthrough

### Student Class
Handles individual student data with a clean `display()` method for output formatting.

### StudentManagementSystem Class
Central controller managing all operations:
- Object storage in list
- Duplicate ID prevention
- CRUD operations implementation

##  How to Run

```bash
python main.py
```

### Quick Start & Demo
```
----- STUDENT MANAGEMENT SYSTEM -----
1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Highest Marks Student
7. Exit

Enter Choice: 1
Enter Student ID: 1
Enter Name of Student: Shaurya
Enter Marks of Student: 99
Enter Age of Student: 20
Student added successfully

Enter Choice: 1
Enter Student ID: 2
Enter Name of Student: Alavya
Enter Marks of Student: 99
Enter Age of Student: 20
Student added successfully

Enter Choice: 2

----- STUDENT RECORDS -----
ID: 1 Name: Shaurya Age: 20 Marks: 99.0
-------------------------
ID: 2 Name: Alavya Age: 20 Marks: 99.0
-------------------------

Enter Choice: 3
Enter Student ID to search: 2
Student Found
ID: 2 Name: Alavya Age: 20 Marks: 99.0

Enter Choice: 4
Enter Student ID: 1
Enter New Marks: 100
Marks Updated

Enter Choice: 6

----- TOPPER -----
ID: 1 Name: Shaurya Age: 20 Marks: 100.0

Enter Choice: 5
Enter Student ID to delete: 2
Student Removed

Enter Choice: 7
Exiting Program...
```

## Learning Outcomes

-  Master Classes and Objects
-  Implement Constructors effectively
-  Work with Lists as Object Storage
-  Build complete CRUD Operations
-  Apply OOP in Real Projects

##  Key Concepts Covered

| Concept | Implementation |
|---------|---------------|
| Classes & Objects | `Student`, `StudentManagementSystem` |
| Constructors | `__init__()` method |
| List Operations | append, remove, iteration |
| User Input Handling | `input()`, type conversion |
| Control Flow | while loop, if-elif-else |

## Contributing

Feel free to fork this project and add enhancements

## License

This project is for educational purposes. Use freely for learning!

---

Made with ❤️ by Shaurya | Happy Coding! 🐍
