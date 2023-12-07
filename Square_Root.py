import cmath

a = int(input("Enter the number "))
b = int(input("Enter the number "))
c = int(input("Enter the number "))

d = (b**2)-(4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print("the roots are", root1, "and" ,root2)