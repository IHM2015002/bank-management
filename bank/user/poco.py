from enum import Enum
import os
import secrets

class Role(Enum):
    CUSTOMER = "CUSTOMER"
    EMPLOYEE = "EMPLOYEE"
    MANAGER = "MANAGER"

class TokenConstants:
    SECRET_KEY = secrets.token_hex(32)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60