from datetime import datetime
from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import VARCHAR

Base = declarative_base()

class StudentGrades(Base):
    __tablename__ = 'Student_grades'
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR(25))
    english = Column(Integer)
    hindi = Column(Integer)
    maths = Column(Integer)
    Added_on = Column(DateTime,default=datetime.now())

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR(25))
    father_name = Column(VARCHAR(25))
    mother_name = Column(VARCHAR(25))
    roll_no = Column(String(20),unique=True)
    classs = Column(String(15))
    section = Column(String(5))

if __name__ == '__main__':
    engine = create_engine('sqlite:///student.db',echo = True)
    Base.metadata.create_all(engine)