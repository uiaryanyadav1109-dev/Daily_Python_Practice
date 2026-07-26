#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1*num2<=1000:
    result=num1*num2
    print("The result is:", result)
elif num1*num2>1000:
    result=num1+num2
    print("The result is:", result)
else:
    print("ERROR")