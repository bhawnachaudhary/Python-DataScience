from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from StudentDB import Student,Base,StudentGrades
import os

Session = sessionmaker(bind=create_engine('sqlite:///student.db'))

# DATABASE MENU FOR USER
def database_menu():
    os.system('cls') # clears previous output
    print('''
    1. Add a Student
    2. View all the students
    3. Add student's grades
    4. View Student's grades
    5. Update Student's grades
    6. Delete a Student
    7. Exit
    ''')
    choice = input('Enter your choice: ')
    return choice




def add_student():
    global Session  # make a outer variable accessible inside a function

    print("ENTER DETAIL OF STUDENT")
    name = input("👨‍🎓 name:")
    fname = input("👨‍🎓 father's name:")
    mname = input("👨‍🎓 mother's name:")
    rollno = input("👨‍🎓 roll num:")
    classs = input("👨‍🎓 class:")
    section = input("👨‍🎓 section:")

    if name and fname and mname and rollno and classs and section:
        std = Student(name=name, father_name=fname, 
                      mother_name=mname,roll_no =rollno,
                      classs = classs, section=section)           # 1. create object
        db = Session()                                          # 2. open database
        db.add(std)                                             # 3. add object to db
        db.commit()                                             # 4. save database
        db.close()                                              # 5. close database
        print('👨‍🎓 Student added successfully ✔')
    else:
        print('invalid details')
        print('name:',name)
        print('father:',fname)
        print('mother:',mname)
        print('rollno:',rollno)
        print('class and section:',classs,section)


def view_all_students():
    global Session
    db = Session()
    results = db.query(Student).all()
    for std  in results:
        print(std.roll_no,std.name)
    input('press enter to continue ')



def delete_student():
    global session
    roll_num = input("Student's Roll Number: ")
    if roll_num:
        db = session()
        student = db.query(Student).filter(Student.roll_num==roll_num)
        student.delete()
        db.commit()
        db.close()
        print("STUDENT REMOVED FROM THE DB")
    else:
        print('INVALID VALUE PASSED AS roll number')
    input('Press ENTER to continue...')




#main loop
while True:
    ch = database_menu()
    if ch == '1':
        add_student()
    elif ch == '2':
        view_all_students()
    elif ch == '3':
        add_student_grades()
    elif ch == '4':
        view_student_grades()
    elif ch == '5':
        update_student_grades()
    elif ch == '6':
        delete_student()
    elif ch == '7':
        print('Closing Program. Bye Bye ')
        break
    else:
        print('Wrong Choice')