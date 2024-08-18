

def check_substring():
    str1 = input("Enter the main string: ")
    str2 = input("Enter the substring: ")
    if str2 in str1:
        print("The string is a substring.")
    else:
        print("The string is not a substring.")

def count_occurrences():
    str1 = input("Enter the string: ")
    char = input("Enter the character: ")
    print("The character occurs", str1.count(char), "times.")

def replace_substring():
    str1 = input("Enter the main string: ")
    str2 = input("Enter the substring to replace: ")
    str3 = input("Enter the new substring: ")
    print(str1.replace(str2, str3))

def convert_to_capital():
    str1 = input("Enter the string: ")
    print(str1.upper())

while True:
    print("\nMenu:")
    print("1. Check if the String is a Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a substring with another substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_substring()
    elif choice == 2:
        count_occurrences()
    elif choice == 3:
        replace_substring()
    elif choice == 4:
        convert_to_capital()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")