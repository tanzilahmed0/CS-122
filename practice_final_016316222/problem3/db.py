''' : Define SQLAlchemy Base and a model ExpenseModel for table expenses with
columns for amount, category, date, and description.
• 3: Write init_db() to create expenses.db and return a Session.
• 4: Write save_expense(expense, session) to insert a record.
• 5: Write get_expenses(session) to return a list of Expense objects from all records. ''' 

from unicodedata import category
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from expense import Expense 
from tracker import ExpenseTracker

Base = declarative_base()

class ExpenseModel(Base): 
    __tablename__ = 'expenses'
    amount = Column(Integer, primary_key=True) 
    category = Column(String)
    date = Column(Date)
    description = Column(String) 


def init_db(): 
    engine = create_engine('sqlite:///expenses.db')
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    return Session()

def save_expense(expense, session): 
    e = ExpenseModel(
        amount = expense.amount,
        category = expense.category,
        date = expense.date,
        description = expense.description      
    )
    session.add(e)
    session.commit()

def get_expenses(session): 
    rows = session.query(ExpenseModel).all()
    output = []

    for row in rows: 
        output.append(Expense(row.amount, row.category, row.date, row.description))

    return output


