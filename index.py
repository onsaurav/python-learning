import sys
from person import Person, Student
from classexample import C1, C2, C3

#This is the first .py file of this tutorial
""" 
This is another way of comment in Python.
I want top go through a complete learning carriculum. 
"""

print("Hi, I am working in Python now!")
print(sys.version)

#exit()

p1 = Person("Saurav", 40)
print(p1)
print(p1.creditLimit())

s1 = Student("Kartik", 20, "CSE")
print(s1)
s1.show()

student2 = C3("Parth Sarothi", 18, "Artificial Engineering")
print(student2)
student2.show()
student2.position()






