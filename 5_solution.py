# Findind the first non repeating character in a word
string=input("Enter a word: ")
for char in string:
    if string.count(char) == 1:
        print(f"First non repeated character is {char}")
        break