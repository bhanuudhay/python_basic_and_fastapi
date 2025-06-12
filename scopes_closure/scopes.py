username = "bhanu"
def func():
    #username = "udhay"
    print(username)
    

print(username)
func()

x = 99
def funct2(y):
    z = x + y
    return z
print(funct2(1))


def funct3():
    global x #iska matlab ham x ko globally le kar aa gye hai ab sirf usme change hoga
    x = 12

funct3()
print(x)


def f1():
    x = 88
    def f2():
        print(x)
    return f2
f1()()

def chai(num):
    def actual(x):
        return x ** num
    return actual