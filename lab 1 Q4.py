n=int(input("Enter an number:"))
print("The divisors of the number are:")
for x in range(1,n+1):
    if(n%x==0):
        print(x)