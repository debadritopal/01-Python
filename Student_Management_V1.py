students=[]
def add_student():
    name=input("Enter Student name: ")
    name=name.strip().title()
    if(name in students):
        print("Name already exists in record")
    elif not name:
        print("Please enter a valid name")
    else:
        students.append(name)
def view_student():
    if students:
         str="="*40
         print(str,"Student List",str,sep='\n')
         for index,student in enumerate(students,start=1):
             print(f"{index}.{student}")
    else:
        print("No records yet")
def search_student():
    name=input("Enter name ")
    name=name.strip().title()
    if name in students:
        print("Record exists")
        print(f"Position: {students.index(name)+1}")
    else:
        print("Record doesn't exist")
def delete_student():
    name=input("Enter name ")
    if name in students:
        students.remove(name)
        print("Record deleted")
    else:
        print("Record not found")
print("="*40,"Student Manager","="*40,sep='\n')
while True:
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