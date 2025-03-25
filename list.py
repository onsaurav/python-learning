fruits = ["Mango", "Litchi", "Apple", "Orange", "Graps"]
print(fruits)

fruits.insert(2, "Benana")
print(fruits)

fruits[3] = "Stobery"
print(fruits)

fruits.append("apple")
print(fruits)

newFruits = ["Coconut", "Pinaple", "Blue-Berry"]
print(newFruits)

fruits.extend(newFruits)
print(fruits)

newArrivel = ("Olive","Amla")
fruits.extend(newArrivel)
print(fruits)

fruits.remove("Stobery")
print(fruits)

fruits.pop(5)
print(fruits)

fruits.pop()
print(fruits)

del fruits[3]
print(fruits)
