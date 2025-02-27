a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
R=(lambda a,b:a if a>b else b)
print("Greater number is",R(a,b))