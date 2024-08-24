# Multiplication table of given number bur skip 5 iteration
num=int(input("Enter a number: "))
for i in range (1,11):
    if i == 5 :
        continue
    print(f"{num} * {i} = {num*i}")