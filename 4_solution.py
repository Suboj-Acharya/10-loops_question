# Reverse a string using loop
string=input("Enter a word: ")
rev_str=""
for char in string:
    rev_str = char + rev_str
print(f"Your reverse word is {rev_str}")    