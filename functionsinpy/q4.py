import math

def area_circle(r):
    area = math.floor(math.pi * r ** 2)
    circum = math.floor(2 * math.pi * r)
    return area, circum

a ,c = area_circle(5)
print(a,c)
