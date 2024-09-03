
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice=int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    print("Result: ", a+b)
elif choice == 2:
    print("Result: ", a-b)
elif choice == 3:
    print("Result: ", a*b)
elif choice == 4:
    if b!= 0:
        print("Result: ", a/b)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")