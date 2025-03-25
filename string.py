txt = "The best things in life are free!"
print("best" in txt)

print(txt[5:11])
print(txt[:10])
print(txt[10:])
print(txt[-5: -2])

parts = txt.split(" ")
for part in parts:
    print(part)

age = 40
name = "Saurav Biswas"

print(f"Mr. {name}, age {age}")

print(f"The word \"Best\" search result index is : {txt.find("best")}")


nickName = "Saurav"
firstname, middleName, lastName = "Kartik", "Chandra", "Biswas"
favouriteFruits = ["Mango", "Litchi", "Apple", "Orange", "Graps"]

print("Age: " , age , ", Name: " , nickName)

fullName = "{fName} {mName} {lName}".format(fName = firstname, mName = middleName, lName = lastName)
print("Fullname  is {flName}".format(flName = fullName))

#for x in fullName:
#    print(x)

if ("and" in fullName):
    print("AND exist in fullname")