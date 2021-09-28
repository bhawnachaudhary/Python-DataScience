from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from StudentDB import Student,Base,StudentGrades

Session = sessionmaker(bind=create_engine('sqlite:///student.db'))

# DATABASE MENU FOR USER
def database_menu():
    print('''
    1. Add a Student
    2. View all the students
    3. View Student's grades
    4. Update Student's grades
    5. Delete a Student
    6. Exit
    ''')
    choice = input('Enter your choice: ')
    return choice