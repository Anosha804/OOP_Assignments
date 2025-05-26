# 17. Class Decorators
# Assignment: Create a class decorator add_greeting that modifies a class to add a greet() method 
# returning "Hello from Decorator!". Apply it to a class Person.


class add_greeting:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        instance = self.cls()
        instance.greet = lambda: "Hello from Decorator!"
        return instance

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())