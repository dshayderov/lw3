import math
print("Area of triangle")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
p = (a+b+c)/2
s = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print("s = %.2f" % (s))
