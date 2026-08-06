# Write a program that takes a year as input and determines if it is a leap year.
year=int(input("Enter The Year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")