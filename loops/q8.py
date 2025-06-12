item = ["apple", "banana", "cherry", "date", "elderberry", "apple"]
for el in item:
    if(item.count(el) > 1):
        print("Not Unique")
        print(el)
        break
else:
    print("Unique")
