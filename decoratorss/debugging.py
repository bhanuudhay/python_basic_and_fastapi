def debug(func):
    def wrapper(*args,**kwargs):
        print(args,kwargs)
        print(func.__name__)
        return func(*args,**kwargs)
        
    return wrapper

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting} , {name}")

greet("chai", greeting="hi")