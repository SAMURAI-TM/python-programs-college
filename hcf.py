#hcf
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
while (n !=m):
    if n>m:
        num=n-m
    else:
        num=m-n
    print ("The HCF is",num)
    break