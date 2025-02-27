n=int(input("Enter the number to find factorial : "))
s=lambda n:1 if n==0 else n*s(n-1)
print("Factorial",s(n))