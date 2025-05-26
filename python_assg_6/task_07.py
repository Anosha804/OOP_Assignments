# 7. Access Modifiers: Public, Private, and Protected
# Assignment: Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

emp = Employee("John", 50000, "123-45-6789")

print(emp.name)        # ✅ Public: Accessible
print(emp._salary)     # ✅ Protected: Accessible but not recommended
print(emp.__ssn)     # ❌ Private: Not directly accessible
print(emp._Employee__ssn)  # ✅ Can be accessed using name mangling