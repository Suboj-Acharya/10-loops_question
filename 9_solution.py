# List uniqueness checker
list1=[]
for i in range(1,6):
    fruit=input("Enter names of fruit: ")
    list1.append(fruit)
for a in list1:
    if (list1.count(a) > 1 ) :
        break
print(f"Duplicate item is {a}")    