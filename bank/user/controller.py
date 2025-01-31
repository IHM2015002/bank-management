from fastapi import APIRouter, Body, Depends, status
from .model import Contracts, User
from .service import UserService
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from ..exception import DuplicateFoundException


user_router = APIRouter()

def get_user_service():
    return UserService()

@user_router.post('/register')
def registration(
    body: Contracts.Registration = Body(...),
    service: UserService = Depends(get_user_service)
):
    try:
        resp = service.regiter(body=body)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_201_CREATED)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)


@user_router.post('/login')
def login(
    body: Contracts.Login = Body(...),
    service: UserService = Depends(get_user_service)
):
    try:
        resp = service.login(body.email, body.password)
        return JSONResponse(jsonable_encoder(resp), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse({'error':e.args[0]}, status_code=status.HTTP_400_BAD_REQUEST)

