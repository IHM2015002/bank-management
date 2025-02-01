from fastapi import APIRouter, status, Body, Depends
from fastapi.responses import JSONResponse
from .service import EmployeeService
from fastapi.encoders import jsonable_encoder
from .model import EmployeeRequest
from ..exception import NotFoundException
from ..authentication.authentication import UserAuthentication
from ..user.poco import Role
from ..user.model import User

employee_router = APIRouter()

def get_employee_service():
    return EmployeeService()

def user_authentication(required_roles=[Role.MANAGER]):
    def dependency(token: str = Depends(UserAuthentication().oauth_scheme)):
        print(token)
        return UserAuthentication().get_current_user(required_roles=required_roles, token=token)
    return dependency

@employee_router.get('/{emp_id}')
def get_employee_by_id(
        emp_id: str, 
        service: EmployeeService = Depends(get_employee_service),
        manager: User = Depends(user_authentication([Role.MANAGER]))
    ):
    try:
        resp = service.get_employee(emp_id, manager.id)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_200_OK)
    except NotFoundException as e:
        return JSONResponse(content=e.args, status_code=status.HTTP_404_NOT_FOUND)

@employee_router.get('')
def get_all_employee(
        service: EmployeeService = Depends(get_employee_service),
        manager: User = Depends(user_authentication([Role.MANAGER]))
    ):
    try:
        print(manager.id)
        resp = service.get_all_employee(manager.id)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_200_OK)
    except NotFoundException as e:
        return JSONResponse(content=e.args, status_code=status.HTTP_404_NOT_FOUND)

@employee_router.post('/add')
def add_employee(
    body: EmployeeRequest = Body(...), 
    service: EmployeeService = Depends(get_employee_service), 
    manager: User = Depends(user_authentication([Role.MANAGER]))
):
    try:
        resp = service.add_employee(body, manager.id)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content=e.args, status_code=status.HTTP_404_NOT_FOUND)