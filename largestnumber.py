a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
elif c>=a and c>=b:
    print(c)
else:
    print("enter different numbers!")

