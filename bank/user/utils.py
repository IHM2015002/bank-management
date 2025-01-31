from fastapi import Depends
import bcrypt
from fastapi.exceptions import HTTPException
from .poco import TokenConstants
from datetime import datetime, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer
from .dal import UserDAL

class UserUtils:

    oauth_scheme = OAuth2PasswordBearer(tokenUrl='/login')

    def __init__(self):
        self.user_dal = UserDAL()

    def get_hashed_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=password.encode('utf-8'), salt=salt)
        return hashed_password.decode('utf-8')
    
    def verify_password(self, password: str, db_password: str) -> bool:
        return bcrypt.checkpw(password=password.encode('utf-8'), hashed_password=db_password.encode('utf-8'))
    
    def create_access_token(self, email: str, role: str):
        to_encode = {'email': email, 'role': role}
        to_encode.update({'exp': datetime.now() + timedelta(minutes=TokenConstants.ACCESS_TOKEN_EXPIRE_MINUTES)})
        encoded_jwt = jwt.encode(to_encode, TokenConstants.SECRET_KEY, algorithm=TokenConstants.ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, TokenConstants.SECRET_KEY, algorithms=TokenConstants.ALGORITHM)
            return payload
        except Exception:
            raise HTTPException(detail='Please pass valid token', status_code=401)
    
    def get_current_user(self, required_roles: list[str], token: str = Depends(oauth_scheme)):
        payload = self.verify_token(token=token)
        email = payload.get('email')
        if not email:
            raise HTTPException(detail='invalid token', status_code=401)
        user = self.user_dal.is_user_exist(email=email)
        if not user:
            raise HTTPException(detail='user not exist', status_code=401)
        if user.role.name not in required_roles:
            raise HTTPException(detail='you do not have permission', status_code=401)
        return user