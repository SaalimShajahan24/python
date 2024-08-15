count = 0
total = 0

for num in range(101, 200):
    if num % 7 == 0:
        count += 1
        total += num

print("Number of integers:", count)
print("Sum of integers:", total)