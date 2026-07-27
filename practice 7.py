word=input("enter a string:").lower()
print("ORIGINAL STRING:",word)
vowels="aeiou"
count=0
for char in word:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
