from sqlalchemy.orm import Session
from .model import Employee, EmployeeRequest
from ..db_conn.connect import get_db_service
from sqlalchemy import or_


class EmployeeDAL:
    def __init__(self):
        self.db: Session = get_db_service()


    def create_employee(self, body: EmployeeRequest, manager_id: int):
        emp = Employee(
            name=body.name,
            email=body.email,
            phone=body.phone,
            designation=body.designation,
            manager_id=manager_id
        )
        self.db.add(emp)
        self.db.commit()
        self.db.refresh(emp)
        return emp

    def get_emp_by_id(self, emp_id: str, manager_id: int):
        return self.db.query(Employee).filter(Employee.id==emp_id, Employee.manager_id==manager_id).first()
    
    def is_emp_exist(self, email: str, phone: str):
        return self.db.query(Employee.id).filter(or_(Employee.email==email, Employee.phone==phone)).first()
    
    def get_all_emp_by_manager_id(self, manager_id: int):
        return self.db.query(Employee).filter(Employee.manager_id==manager_id).all()
        

