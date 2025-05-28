class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name #public variable
        self._salary = salary #protected variable
        self.__ssn = ssn #private variable

emp = Employee("Ali", 3000, 1234-56-890)
#access public variable
print("Public Variable:", emp.name)
#access protected variable
print("Protected Variable:", emp._salary)
#access private variable
try:
    print("Private Variable:", emp.__ssn)
except AttributeError:
    print("Cannot access private variable __ssn.")