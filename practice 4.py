#Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
a=int(input("enter the integer:"))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print(f"factorial of {a} is {factorial}")
    