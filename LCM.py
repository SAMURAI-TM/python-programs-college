#LCM
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
if(n>m):
    maximum=n
else:
    maximum=maximum
while(True):
    if (maximum % n==0 and maximum % m==0):
        print("\n LCM of {0} and {1}={2}". format (n,m,maximum))
        break
    maximum = maximum+1