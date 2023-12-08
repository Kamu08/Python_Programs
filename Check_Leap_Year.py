num = int(input("Enter the year "))
if (num % 400 == 0) and (num % 100 == 0):
    print(f"{num} is a leap year")
elif (num % 4 == 0) and (num % 100 != 0):
    print(f"{num} is a leap year")
else:
    print("It is not a leap year")