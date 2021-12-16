person = {} #empty dictionary
person["name"] = "Shiv"
person["surname"] = "Patel"
person["weight"] = 80.22
print(person)
person["gender"] = True 
person["name"] = "Shankar"
print(person)
print(person.get("name"))
print(person.get("dob"))
print(person.get("location"))
print(person.get("surname"))
person.pop("weight")
print(person)
removed_value = person.popitem()
print("removed value ",removed_value)
print(person)
person.update({"surname":"PATEL","location":"Kaliash"})
print(person)
keys = person.keys() #it will return all keys from dictionary
print(keys)
values = person.values() #it will return all values 
print(values)
person.clear()
print(person)