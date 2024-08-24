# Take input from user until input is from 1 to 10
num = int(input("Enter a number: "))
while (True):
    if (num >= 1 and num <= 10 ) :
        print("Welcome to the coding world")
        break
    else:
        print("Try again,Enter number between 1 to 10 ")
        num = int(input("Enter a number: ")) 
        continue   
       