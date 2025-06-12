def print_kwargs(**args):
    for key , value in args.items():
        print(key,value)

print_kwargs(name="Bhanu", power="100")
print_kwargs(name="Udhay")
print_kwargs(name="Singh" , power="90", enemy = "lazer" ) 

