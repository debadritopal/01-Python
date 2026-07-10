class Student:
    def __init__(self, name, age, branch, semester, cgpa):
        self.name = name
        self.age = age
        self.branch = branch
        self.semester = semester
        self.cgpa = cgpa
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {self.branch}")
        print(f"Semester: {self.semester}")
        print(f"CGPA: {self.cgpa}")
    def update_cgpa(self,cgpa):
        self.cgpa=cgpa
    def update_branch(self,branch):
        self.branch=branch
s1=Student("Debadrito Pal",18,"CSE",1,9.5)
s2=Student("Barnali Roy",18,"BT",1,9.6)
Student.display(s1)
Student.display(s2)
Student.update_branch(s1,"EE")
Student.update_branch(s2,"IT")
Student.update_cgpa(s1,9.8)
Student.update_cgpa(s2,9.9)
Student.display(s1)
Student.display(s2)