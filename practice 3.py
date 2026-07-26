# Display only those characters which are present at an even index number in given string.
word=input("ENTER THE WORD :")
print("Original String is :", word)
print("Printing only even index chars :")
word_len=word[0::2]
for char in word_len:
    print(char)