keys = ['name','surname','gender','age','weight','nationlity']
print(keys)

#creating dictinary using list value as keys 
value = 0
person = dict.fromkeys(keys,value)
print(person)

#copy dictionary into another dictionary 
person_copy = person.copy()
print(person_copy)
person['name'] = "Ankit"
person_copy['surname'] = "Patel"
print("after changing both dictionary let see what they have")
print(person)
total = len(person)
print("total items in person ",total)
print(person_copy)