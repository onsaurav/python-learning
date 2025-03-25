def my_function(fname):
    print(f"Hi {fname}, this is from a function")

my_function("Saurav")

def my_function(*guests):
    print(guests)

my_function("Saurav", "Sachin", "Rahul")

def my_function(*args, **kwargs):
    print("Positional args (tuple):", args)
    print("Keyword args (dict):", kwargs)

my_function(1, 2, 3, name="Alice", age=25)

x = lambda a: a + 10
print(x(5))

x = lambda a,b: a * b
print(x(5, 7))

def myFunc(n):
    return lambda a: (a/2) + n

funCall = myFunc(8)
print(funCall(5))


