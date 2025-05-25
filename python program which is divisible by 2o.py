#python program which is divisible by 2or 5 B/W upper and lower limit
a=0
n=int(input("Enter the lower limit:"))
m=int(input("Enter the upper limit:"))
print("number is divisible:")
for a in range(n,m):
    if a%2==0 or a%5==0:
    
        print(a)