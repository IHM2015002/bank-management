from fastapi import APIRouter, status, Body, Depends
from fastapi.responses import JSONResponse
from .service import EmployeeService
from fastapi.encoders import jsonable_encoder
from .model import EmployeeRequest
from ..exception import NotFoundException
from ..user.utils import UserUtils
from ..user.model import User

employee_router = APIRouter()

# Instantiate the classes

def get_employee_service():
    return EmployeeService()

def get_user_utils(required_roles=['MANAGER']):
    def dependency(token: str = Depends(UserUtils().oauth_scheme)):
        print(token)
        return UserUtils().get_current_user(required_roles=required_roles, token=token)
    return dependency

@employee_router.get('/{emp_id}')
def get_employee_by_id(
        emp_id: str, 
        service: EmployeeService = Depends(get_employee_service), 
        user_info: User = Depends(get_user_utils(['MANAGER']))
    ):
    try:
        resp = service.get_employee(emp_id)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_200_OK)
    except NotFoundException as e:
        return JSONResponse(content=e.args, status_code=status.HTTP_404_NOT_FOUND)

@employee_router.post('/add')
def add_employee(
    body: EmployeeRequest = Body(...), 
    service: EmployeeService = Depends(get_employee_service), 
    user_info: User = Depends(get_user_utils(['MANAGER']))
):
    resp = service.add_employee(body)
    return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_201_CREATED)
