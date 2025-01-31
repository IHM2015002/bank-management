from sqlalchemy import Column, Integer, String, DateTime, Enum
from pydantic import BaseModel, Field, EmailStr, field_validator
from ..db_conn import Base
from datetime import datetime
from .poco import Role



class User(Base):

    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    phone = Column(String(30), nullable=False, unique=True)
    role = Column(Enum(Role), nullable=False, default=Role.CUSTOMER)
    password = Column(String(100), nullable=False)
    created_on = Column(DateTime, default=datetime.now())
    updated_on = Column(DateTime)



class Contracts:

    class Registration(BaseModel):
        name: str
        email: EmailStr
        phone: str = Field(...,pattern=r'^\d{10}$')
        role: Role
        password: str = Field(..., min_length=8)

        @field_validator('password')
        def validate_password(cls, password):
            if not any(char.isupper() for char in password):
                raise ValueError('password should have atleast one upper case char')
            if not any(char.isdigit() for char in password):
                raise ValueError('password should have atleast one digit case char')
            if not any(not char.isalnum() for char in password):
                raise ValueError('password should have atleast one special char')
            if not any(char.islower() for char in password):
                raise ValueError('password should have atleast one lower case char')
            
            return password


    
    class Login(BaseModel):
        email: EmailStr
        password: str

    class LoginResponse(BaseModel):
        token: str
        token_type: str = 'bearer'

    class RegistrationResponse(BaseModel):
        id: int
        name: str
        email: str
        phone: str
        role: Role