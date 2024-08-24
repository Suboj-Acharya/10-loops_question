# Sum of even numbers
sum_ev=0
num=int(input("Enter end number: "))
for i in range (1,num+1):
    if (i % 2 == 0) :
        sum_ev=sum_ev+i
print(f"Sum of even numbers for 1 to {num} is {sum_ev}. ")