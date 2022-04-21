print("Enter the numbers")
a3 = int(input("a3 = "))
a2 = int(input("a2 = "))
a1 = int(input("a1 = "))
b2 = int(input("b2 = "))
b1 = int(input("b1 = "))
c1 = (a1+b1)%10
c2 = (a2+b2+(a1+b1)//10)%10
c3 = a3+((a2+b2 + (a1+b1)//10) // 10)
print("Result is {0}{1}{2}".format(c3,c2,c1))