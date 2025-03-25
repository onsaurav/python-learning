fruits = ["Mango", "Litchi", "Apple", "Orange", "Graps", "Coconut", "Pinaple", "Blue-Berry"]

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

[print("--> " + x) for x in fruits]

newlist = [x.upper() for x in fruits if x != "Coconut"]
print(newlist)

newlist.sort()
print(newlist)

mylist = fruits[:]
print(mylist)
