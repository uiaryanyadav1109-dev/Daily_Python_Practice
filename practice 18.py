#Write a program to print the first n terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
num1=0
num2=1
n=int(input("enter a integer(greter than 0 and 1:)"))
for i in range(n):
    print(num1,end=" ")
    res=num1+num2
    num1=num2
    num2=res