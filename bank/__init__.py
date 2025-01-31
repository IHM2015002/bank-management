from fastapi import FastAPI
from .employee.controller import employee_router
from .user.controller import user_router

app = FastAPI()

app.include_router(employee_router, prefix='/employee', tags=['employee'])
app.include_router(user_router, prefix='/user', tags=['user'])
