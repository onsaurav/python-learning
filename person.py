class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} is {self.age} years old")
    
    def creditLimit(self):
        return (self.age/5) * 10000

class Student(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def show(self):
        print(f"{self.name} is a student os {self.subject}")
    
    
    