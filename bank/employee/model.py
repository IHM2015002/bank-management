from sqlalchemy import Integer, String, Column, ForeignKey
from pydantic import BaseModel, Field, EmailStr
from ..db_conn import Base
from ..user.model import User
import uuid

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(String(100), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = Column(String(30), nullable=False)
    phone = Column(String(30), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    designation = Column(String(30))
    manager_id = Column(Integer, ForeignKey(User.id), nullable=True)
    

# To create table in db if not exist but after creation model changes can not push to db table
# Base.metadata.create_all(bind=engine)


class EmployeeResponse(BaseModel):
    emp_id: str
    name: str
    phone: str
    email: EmailStr
    designation: str
    manager_id: int

class EmployeeRequest(BaseModel):
    name: str = Field(...,min_length=1)
    phone: str = Field(..., pattern=r'^\d{10}$')
    email: EmailStr
    designation: str


