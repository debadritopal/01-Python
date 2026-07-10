class Person:
    def __init__(self,name):
        self.name=name
students=[]
teachers=[]
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f"{self.name}"
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f"{self.name}"
line='-'*40
print(line)
print("School Management")
print(line,end='\n')
while True:
    try:
        print("1. View Student\n2. View Teacher\n3. Add Student\n4. Add Teacher\n5. Exit")
        choice=int(input("Enter choice: "))
        if choice==1:
            if students:
                for i in students:
                    student=Student(i)
                    print(student)
            else:
                print("No entries")
        elif choice==2:
            if teachers:
                for i in teachers:
                    teacher=Teacher(i)
                    print(teacher)
            else:
                print("No entries")
        elif choice==3:
            student_name=input("Enter name: ").strip().title()
            if student_name:
                student=Student(student_name)
                students.append(student)
            else:
                print("Enter a valid name")
        elif choice==4:
            teacher_name=input("Enter name: ").strip().title()
            if teacher_name:
                teacher=Teacher(teacher_name)
                teachers.append(teacher)
            else:
                print("Enter a valid name")
        elif choice==5:
            print("Exiting School Management System....")
            break
        else:
            print("Enter a valid choice")
    except:
        print("Enter an integer")