person = {"name":"bhanu","age":20,"city":"india"}
print(person["name"])
print(person.get("age")) # get ka yeh benefit hai ki agar key nahi hai toh error nahi dekhega
for el in person:
    print(el , person[el])
for key , value in person.items(): # another way to print the dictionary
    print(key , value)
print(len(person))

print(person.pop("age"))

print(person)

organisation = {
    "person1":{"name":"bhanu","age":20,"city":"india"},
    "person2":{"name":"udhay","age":21,"city":"india"},
    }

print(organisation["person1"])
print(organisation["person2"])
print(organisation["person1"]["name"]) # get directky access to the value of the key

