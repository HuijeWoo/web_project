from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def __str__(self) :
        return f'id: {id}, email: {self.name}, name: {self.email}'

class Dept(Base):
    __tablename__ = "depts"
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    deptno = Column(Integer, primary_key=True)
    dname = Column(String(128))
    loc = Column(String(128))

    def __init__(self, deptno, dname, loc):
        self.deptno = deptno
        self.dname = dname
        self.loc = loc    
    
    def __str__(self) :
        return f'deptno: {self.deptno}, dname: {self.dname}, loc: {self.loc}'