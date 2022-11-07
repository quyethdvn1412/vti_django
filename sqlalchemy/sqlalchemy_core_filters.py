from sqlalchemy import MetaData, Table, Column, String, Integer
from sqlalchemy import Text, DateTime, Boolean, create_engine, select, insert, update, delete, or_, and_

connection_string = "sqlite:///Northwind_small.sqlite"
engine = create_engine(connection_string, echo=False)

metadata = MetaData()
employees = Table(
    'Employee', metadata, 
    Column('Id', Integer(), primary_key=True),
    Column('LastName', String(8000)), 
    Column('FirstName', String(8000)), 
    Column('BirthDate', String(8000))
)

def print_result(stmt):
    with engine.connect() as con:
        rs = con.execute(stmt)
        for row in rs:
            print(row)

def select_all():
    stmt = employees.select()
    # stmt = select(employees)
    print_result(stmt)

def select_equals():
    stmt = employees.select().\
        where(employees.c.Id == 1)
    print_result(stmt)

def select_not_equals():
    stmt = employees.select().\
        where(employees.c.Id != 1)
    print_result(stmt)

def select_greather_than():
    stmt = employees.select().\
        where(employees.c.Id > 5)
    print_result(stmt)

def select_less_than():
    stmt = employees.select().\
        where(employees.c.Id < 3)
    print_result(stmt)

def select_like():
    stmt = employees.select().\
        where(
            employees.c.LastName.like("Pe%k")
            )
    print_result(stmt)

def select_not_like():
    stmt = employees.select().\
        where(
            employees.c.LastName.not_like("Pe%k")
            )
    print_result(stmt)

def select_contains():
    stmt = employees.select().\
        where(
            employees.c.LastName.contains("u")
            )
    print_result(stmt)

def select_startswith():
    stmt = employees.select().\
        where(
            employees.c.LastName.startswith("D")
        )
    print_result(stmt)

def select_endswith():
    stmt = employees.select().\
        where(
            employees.c.LastName.endswith("n")
        )
    print_result(stmt)

def select_in_():
    stmt = employees.select().\
        where(
            employees.c.Id.in_([1, 2, 3])
        )
    print_result(stmt)

def select_not_in():
    stmt = employees.select().\
        where(
            employees.c.Id.not_in([1, 2, 3])
        )
    print_result(stmt)

def select_with_python_and():
    stmt = employees.select().\
        where(
            employees.c.LastName.startswith("D")
        )
    print_result(stmt)