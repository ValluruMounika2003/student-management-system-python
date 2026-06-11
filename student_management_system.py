students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    if roll_no in students:
        print("\nStudent Found")
        print("Roll No:", roll_no)
        print("Name:", students[roll_no]["name"])
        print("Marks:", students[roll_no]["marks"])
    else:
        print("Student not found!")


def update_marks():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        new_marks = float(input("Enter New Marks: "))
        students[roll_no]["marks"] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def view_students():
    if len(students) == 0:
        print("No students available!")
        return

    print("\n----- Student Records -----")

    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print("----------------------")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        view_students()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")