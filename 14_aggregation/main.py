class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employee(self):
        print(f"Employee is department: {self.employee.name}")

emp = Employee("Ali")
dept = Department(emp)
dept.show_employee()