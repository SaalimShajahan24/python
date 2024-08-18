def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    rev_n = int(str(n)[::-1])
    return n + rev_n

def solve(n):
    while not is_palindrome(n):
        n = reverse_and_add(n)
    return n

num = int(input("Enter a number: "))
result = solve(num)
print("The resulting palindrome is:", result)