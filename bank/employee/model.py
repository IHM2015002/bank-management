from sqlalchemy import Integer, String, Column, UUID
from pydantic import BaseModel
from ..db_conn import Base, engine
import uuid

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(String(100), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = Column(String(30), nullable=False)
    phone = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    designation = Column(String(30))
    department_id = Column(Integer)
    

# To create table in db if not exist but after creation model changes can not push to db table
# Base.metadata.create_all(bind=engine)


class EmployeeResponse(BaseModel):
    emp_id: str
    name: str
    phone: str
    email: str
    designation: str
    department_id: int

class EmployeeRequest(BaseModel):
    name: str
    phone: str
    email: str
    designation: str
    department_id: int


