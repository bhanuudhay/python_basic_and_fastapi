#measure the time taken to run a function
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        end = time.time()
        print(f"{func.__name__} ran  in {end-start} time ")
        return func(*args,**kwargs)
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
