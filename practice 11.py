#Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
def palindrome(number):
    print("ORGINAL NUMBER:",number)
    orginal_str=str(number)
    reversed_str=orginal_str[::-1]
    if orginal_str==reversed_str:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

palindrome(121)
palindrome(125)
