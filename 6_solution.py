# Calculating factorial of a given number using while loop
num=int(input("Enter a number: "))
fact=1
a=num
while a > 0 :
    fact=fact*a
    a=a-1
print(f"Factorial of {num} is {fact}")    