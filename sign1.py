e = ""  
p = ""  
data = []  

def su():
    global e, p  
    e = input("Enter email: ")
    if e.endswith("gmail.com"):
        p = input("Enter password: ")
        data.append((e, p))  
        print("Signup successful!")
    else:
        print("invalid email")

def si():
    if input("Enter email: ") == e and input("Enter password: ") == p:
        print("Login successful!")
    else:
        print("Invalid email or password.")

def show_data():
    print("\n Following are the emails with passwords :")
    print(data)

def main():
    while True:
        c = input("\n1. Sign Up\n2. Sign In\n3. Exit\n4. Show All Users\nEnter choice: ")
        if c == '1':
            su()
        elif c == '2':
            si()
        elif c == '3':
            print("Goodbye!")
            break
        elif c == '4':
            show_data()
        else:
            print("Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()