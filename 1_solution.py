# Counting positive no in a list
cou=0
list1=[]
for i in range(1,10):
    a=int(input("Enter a number: "))
    list1.append(a)
for num in list1:
    if (num > 0) :
        cou=cou+1
print(f"Total positive numbers = {cou}")            