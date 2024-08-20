factorial_dict = {}

def factorial(n):
    global factorial_dict
    if n == 0 or n == 1:
        return 1
    elif n in factorial_dict:
        return factorial_dict[n]
    else:
        result = n * factorial(n-1)
        factorial_dict[n] = result
        return result


print(factorial(5))  
print(factorial(3)) 
print(factorial(10)) 
print(factorial_dict) 