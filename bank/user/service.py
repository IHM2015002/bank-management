from .model import Contracts
from ..authentication.authentication import UserAuthentication
from .dal import UserDAL
from .model import User
from ..exception import NotFoundException, DuplicateFoundException
from datetime import datetime

class UserService:

    def __init__(self):
        self.user_dal = UserDAL()
        self.user_auth = UserAuthentication()
        
    def regiter(self, body: Contracts.Registration):
        user = self.user_dal.is_user_exist(body.email, body.phone)
        if user:
            raise DuplicateFoundException('user already exist')
        hashed_password = self.user_auth.get_hashed_password(password=body.password)
        user = User(
            name=body.name,
            email=body.email,
            phone=body.phone,
            role=body.role,
            password=hashed_password,
            updated_on=datetime.now()
        )
        user = self.user_dal.add_user(user)
        return Contracts.RegistrationResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role,
            phone=user.phone,
            created_on=user.created_on,
            updated_on=user.updated_on
        )
    
    def login(self, email: str, password: str) -> Contracts.LoginResponse:
        user = self.user_dal.is_user_exist(email=email)
        if not user:
            raise NotFoundException('Email does not exist')
        is_authenticaed = self.user_auth.verify_password(password, user.password)
        if not is_authenticaed:
            raise NotFoundException('Invalid credentials')
        token = self.user_auth.create_access_token(email, user.role)
        return Contracts.LoginResponse(
            token=token
        )