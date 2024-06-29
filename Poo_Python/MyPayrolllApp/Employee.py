

class Employee:

    employee_id = None
    emp_name = None
    emp_last_name = None
    email = None
    password = None
    salary = None

    def __init__(self, employee_id, emp_name, emp_last_name, email, password, salary):
        self._employee_id = employee_id
        self._emp_name = emp_name
        self._emp_last_name = emp_last_name
        self._email = email
        self._password = password
        self._salary = salary


    @property
    def employee_id(self):
        return self.employee_id


    @employee_id.setter
    def employee_id(self, employee_id):
        self.employee_id = employee_id


    
