file = open("myfile.txt","w")
try:
    file.write("Hello, world!")
finally:
    file.close()

with open("myfile.txt","w") as file:
    file.write("Hello, world!")
