from .model import EmployeeResponse
from .model import EmployeeRequest
from ..exception import NotFoundException
from .dal import EmployeeDAL

class EmployeeService:

    def __init__(self):
        # self.emp_list = []
        self.employee_dal = EmployeeDAL()
    
    def get_employee(self, emp_id: str):
        # print(self.emp_list)
        # if not self.emp_list or emp_id > len(self.emp_list):
            # raise NotFoundException('employee not found')
        
        # emp: EmployeeRequest = self.emp_list[emp_id-1]
        emp = self.employee_dal.get_emp_by_id(emp_id=emp_id)
        if not emp:
            raise NotFoundException('employee not found')
        return EmployeeResponse(
            emp_id=emp_id,
            name=emp.name,
            phone=emp.phone,
            email=emp.email,
            designation=emp.designation,
            department_id=emp.department_id
        )
    
    def add_employee(self, body: EmployeeRequest):
        # self.emp_list.append(body)
        # print(self.emp_list)
        emp = self.employee_dal.create_employee(body)
        return EmployeeResponse(
            emp_id=emp.id,
            name=body.name,
            phone=body.phone,
            email=body.email,
            designation=body.designation,
            department_id=body.department_id
        )
        

# def get_employee_service() -> EmployeeService:
#     if not hasattr(get_employee_service, "_service"):
#         get_employee_service._service = EmployeeService()
#     return get_employee_service._service