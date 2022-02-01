from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import functions as func

DeclarativeBase = declarative_base()


class BaseModel():
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'users'
    first_name = Column(VARCHAR(255), nullable=True)
    last_name = Column(VARCHAR(255), nullable=True)
    email = Column(VARCHAR(255), nullable=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employer(DeclarativeBase, BaseModel):
    __tablename__ = 'employers'
    name = Column(VARCHAR(255), nullable=True)


class Employee(DeclarativeBase, BaseModel):
    __tablename__ = 'employees'
    user_id = Column(INTEGER, ForeignKey('users.id'))
    user = relationship('User')
    employer_id = Column(INTEGER, ForeignKey('employers.id'))
    employer = relationship('Employer')