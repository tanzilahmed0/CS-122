from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    major = Column(String, nullable=False)

engine = create_engine('sqlite:///students.db')

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

