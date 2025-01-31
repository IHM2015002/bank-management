from sqlalchemy.orm import Session
from .model import Employee, EmployeeRequest
from ..db_conn.connect import get_db_service


class EmployeeDAL:
    def __init__(self):
        self.db: Session = get_db_service()


    def create_employee(self, body: EmployeeRequest):
        emp = Employee(
            name=body.name,
            email=body.email,
            phone=body.phone,
            designation=body.designation,
            department_id=body.department_id
        )
        self.db.add(emp)
        self.db.commit()
        self.db.refresh(emp)
        return emp

    def get_emp_by_id(self, emp_id: str):
        return self.db.query(Employee).filter(Employee.id==emp_id).first()

