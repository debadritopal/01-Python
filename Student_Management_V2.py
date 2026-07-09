students={}
student_number=0
add_err=False
def add_student():
    name=input("Enter Student name: ")
    name=name.strip().title()
    duplicate=False
    for i in students:
        if(name==students[i][0]):
            duplicate=True
    if duplicate:
        print("Name already Exists")
        add_err=True
    elif not name:
        print("Please enter a valid name")
        add_err=True
    else:
        age=int(input("Enter Student age: "))
        branch=input("Enter Branch name: ").strip().title()
        semester=int(input("Enter Semester: "))
        cgpa=float(input("Enter cgpa: "))
        students.update({student_number:[name,age,branch,semester,cgpa]})
        add_err=False
def view_student():
    line="-"*40
    for i in students:
        print(line)
        print(f"Student {i}\n")
        print(f"Student Name:\t{students[i][0]}\nAge:\t\t{students[i][1]}\nBranch:\t\t{students[i][2]}\nSemester:\t{students[i][3]}\nCGPA:\t\t{students[i][4]}")
        print(line,end='\n')
def search_student():
    name=input("Enter name ")
    name=name.strip().title()
    stud_no=0
    for i in students:
        if name==students[i][0]:
            print("Record exists")
            stud_no=i
    if stud_no!=0:
        line="-"*40
        print(line)
        print(f"Student {stud_no}\n")
        print(f"Student Name:\t{students[i][0]}\nAge:\t\t{students[i][1]}\nBranch:\t\t{students[i][2]}\nSemester:\t{students[i][3]}\nCGPA:\t\t{students[i][4]}")
        print(line,end='\n')
    else:
        print("Record doesn't exist")
def delete_student():
    name=input("Enter name: ")
    name=name.strip().title()
    stud_no=0
    for i in students:
        if name==students[i][0]:
            print("Record deleted")
            stud_no=i
    if(stud_no!=0):
        del students[stud_no]
    else:
        print("No such record exists")
print("="*40,"Student Manager V2","="*40,sep='\n')
while True:
    if not add_err:
        student_number+=1
    print("\n\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit\n\n")
    try:
         choice=int(input("Choose: "))
         if choice==1:
            add_student()
         elif choice==2:
            view_student()
         elif choice==3:
             search_student()
         elif choice==4:
             delete_student()
         elif choice==5:
            print("Exiting student management")
            break
         else:
             print("Enter a valid option")
    except ValueError:
        print("Enter a valid integer")
        student_number-=1