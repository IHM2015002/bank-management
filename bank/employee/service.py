from .model import EmployeeResponse
from .model import EmployeeRequest
from ..exception import NotFoundException, DuplicateFoundException
from .dal import EmployeeDAL

class EmployeeService:

    def __init__(self):
        # self.emp_list = []
        self.employee_dal = EmployeeDAL()
    
    def get_employee(self, emp_id: str, manager_id: int):
        # print(self.emp_list)
        # if not self.emp_list or emp_id > len(self.emp_list):
            # raise NotFoundException('employee not found')
        
        # emp: EmployeeRequest = self.emp_list[emp_id-1]
        emp = self.employee_dal.get_emp_by_id(emp_id=emp_id, manager_id=manager_id)
        if not emp:
            raise NotFoundException('employee not found')
        return EmployeeResponse(
            emp_id=emp_id,
            name=emp.name,
            phone=emp.phone,
            email=emp.email,
            designation=emp.designation,
            manager_id=emp.manager_id
        )
    
    def get_all_employee(self, manager_id: int):
        emps = self.employee_dal.get_all_emp_by_manager_id(manager_id)
        return emps
    
    def add_employee(self, body: EmployeeRequest, manager_id: int):
        if self.employee_dal.is_emp_exist(body.email, body.phone):
            raise DuplicateFoundException('employee already exist')
        emp = self.employee_dal.create_employee(body, manager_id)
        return EmployeeResponse(
            emp_id=emp.id,
            name=emp.name,
            phone=emp.phone,
            email=emp.email,
            designation=emp.designation,
            manager_id=emp.manager_id
        )
        

# def get_employee_service() -> EmployeeService:
#     if not hasattr(get_employee_service, "_service"):
#         get_employee_service._service = EmployeeService()
#     return get_employee_service._service