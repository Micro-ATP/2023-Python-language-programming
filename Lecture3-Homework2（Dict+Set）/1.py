# 创建一个空的字典
studentGrades = {}

# 添加学生和成绩
def addStudent(name, grade):
    studentGrades[name] = grade
    print(f"学生 '{name}' 的成绩已添加为 {grade}")

# 查找成绩
def findGrade(name):
    if name in studentGrades:
        print(f"学生 '{name}' 的成绩是 {studentGrades[name]}")
    else:
        print(f"找不到学生 '{name}' 的成绩")

# 修改成绩
def updateGrade(name, newGrade):
    if name in studentGrades:
        studentGrades[name] = newGrade
        print(f"学生 '{name}' 的成绩已更新为 {newGrade}")
    else:
        print(f"找不到学生 '{name}' 的成绩")

# 删除成绩
def deleteStudent(name):
    if name in studentGrades:
        del studentGrades[name]
        print(f"学生 '{name}' 的成绩已删除")
    else:
        print(f"找不到学生 '{name}' 的成绩")

# 打印学生和成绩
def printAllStudents():
    for name, grade in studentGrades.items():
        print(f"{name}: {grade}")

# 主程序
while True:
    print("\n学生管理系统")
    print("1. 添加学生成绩")
    print("2. 查找学生成绩")
    print("3. 修改学生成绩")
    print("4. 删除学生成绩")
    print("5. 打印所有学生成绩")
    print("6. 退出")

    choice = input("请选择操作 (1/2/3/4/5/6): ")

    if choice == '1':
        name = input("请输入学生姓名: ")
        grade = input("请输入学生成绩: ")
        addStudent(name, grade)
    elif choice == '2':
        name = input("请输入学生姓名: ")
        findGrade(name)
    elif choice == '3':
        name = input("请输入学生姓名: ")
        newGrade = input("请输入新的成绩: ")
        updateGrade(name, newGrade)
    elif choice == '4':
        name = input("请输入学生姓名: ")
        deleteStudent(name)
    elif choice == '5':
        printAllStudents()
    elif choice == '6':
        print("退出系统。")
        break
    else:
        print("无效的选项，请重新选择。")
