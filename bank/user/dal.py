from .model import Contracts
from sqlalchemy.orm import Session
from ..db_conn.connect import get_db_service
from .model import User
from sqlalchemy import or_

class UserDAL:

    def __init__(self):
        self.db: Session = get_db_service()

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def is_user_exist(self, email: str, phone=None):
        user = self.db.query(User).filter(or_(User.email==email, User.phone==phone)).first()
        return user