class StudentManagementSystem:
    def __init__(self):
        self.studentGrades = {}

    def addStudent(self, name, grade):
        self.studentGrades[name] = grade

    def queryGrade(self, name):
        if name in self.studentGrades:
            return self.studentGrades[name]
        else:
            return "Student not found."

    def updateGrade(self, name, newGrade):
        if name in self.studentGrades:
            self.studentGrades[name] = newGrade
            return "Grade updated successfully."
        else:
            return "Student not found."

    def deleteStudent(self, name):
        if name in self.studentGrades:
            del self.studentGrades[name]
            return "Student deleted successfully."
        else:
            return "Student not found."

    def printAllStudents(self):
        for name, grade in self.studentGrades.items():
            print(f"{name}: {grade}")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Search Grade")
        print("3. Update Grade")
        print("4. Delete Student")
        print("5. Print All Students")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            grade = input("Enter student's grade: ")
            sms.addStudent(name, grade)
            print("Student added successfully.")
        elif choice == "2":
            name = input("Enter student's name: ")
            grade = sms.queryGrade(name)
            print(f"Grade for {name}: {grade}")
        elif choice == "3":
            name = input("Enter student's name: ")
            newGrade = input("Enter new grade: ")
            result = sms.updateGrade(name, newGrade)
            print(result)
        elif choice == "4":
            name = input("Enter student's name: ")
            result = sms.deleteStudent(name)
            print(result)
        elif choice == "5":
            sms.printAllStudents()
        elif choice == "6":
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break
        else:
            print("ERROR. Please try again.")
