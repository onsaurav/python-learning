class C1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #print("C1 initialized")
    
    def show(self):
        print(f"{self.age} years old {self.name}")

class C2:
    def __init__(self, subject):
        self.subject = subject
        #print("C2 initialized")
    
    def position(self):
        print(f"Searching for a position related to {self.subject}")

class C3(C1, C2):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  
        C2.__init__(self, subject)  
        #print("C3 initialized")

    def __str__(self):
        return f"{self.name} is a {self.age} old student, now studying {self.subject}"
    
