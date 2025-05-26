# 14. Aggregation
# Assignment: Create a class Department and a class Employee. Use aggregation by having a Department object store a 
# reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

emp = Employee("Anosha")
dept = Department("Administration", emp)
print(f"{dept.employee.name} works in {dept.dept_name}")