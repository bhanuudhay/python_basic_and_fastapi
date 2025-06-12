inp = int(input("Enter the distance in km: "))
if(inp < 3):
    print("walk")
elif(inp >= 3 and inp <= 15):
    print("Bike")
elif(inp > 15):
    print("Car")
else:
    print("Enter a valid distance")
