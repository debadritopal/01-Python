class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person):
    def __init__(self,name,age,branch,cgpa):
        super().__init__(name,age)
        self.branch=branch
        self.cgpa=cgpa
    def display_student(self):
        super().display()
        print(f"Branch: {self.branch}")
        print(f"CGPA: {self.cgpa}")
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
    def display_person(self):
        super().display()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")