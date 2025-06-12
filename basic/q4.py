inp1 = input("Enter the name of the fruit : ")
inp = input("Enter the color of the fruit :- 'Green' , 'Yellow' , 'Brown' :  ")
if(inp == "Green"):
    print("your " + inp1 + " is Unripe")
elif(inp == "Yellow"):
    print("your " + inp1 + " is Ripe")
elif(inp == "Brown"):
    print("your " + inp1 + " is Overripe")
else:
    print("Enter a valid color")
