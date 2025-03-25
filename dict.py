thisdict = {
    "country":"Bangladesh",
    "district":"Dhaka",
    "place":"Mirpur",
    "amount": 7500
}

print(thisdict)
print(thisdict["place"])
print(thisdict.get("amount"))
print(thisdict.keys())
print(thisdict.values())

if("place" in thisdict):
    print(f"Yes! \"place\" exist in this dictionary")

thisdict["color"] = "red"
print(thisdict)

thisdict["color"] = "purple"
print(thisdict)

print(thisdict.pop("amount"))
print(thisdict)

print(thisdict.popitem())
print(thisdict)

del thisdict["country"]
print(thisdict)

for x in thisdict.keys():
    print(f"{x} --> {thisdict[x]}")

for (x, y) in thisdict.items():
    print(f"{x} => {y}")


nestedDict = {
    "name":"Berselona",
    "country":"SPain",
    "players":{
        "player1": {
            "name": "Leonel Mesi",
            "amount":100000
        },
        "player2": {
            "name": "Xavi",
            "amount":75000
        },
        "player3": {
            "name": "Iniesta",
            "amount":80000
        }
    }
}

print(nestedDict)
print(nestedDict["players"])
print(nestedDict["players"]["player1"]["name"])

