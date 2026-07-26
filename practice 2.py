# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
n=int(input("ENTER THE RANGE:"))
previous_num = 0
for i in range(n+1):
    current_sum = i + previous_num
    
    print(f"Current Number {i} Previous Number {previous_num} ,Sum: {current_sum}")
    
    previous_num = i