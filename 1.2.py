def calculate_bill(units):
    if units <= 200:
        bill = units * 0.50
    elif units <= 400:
        bill = 200 * 0.50 + (units - 200) * 0.65
    elif units <= 600:
        bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
    else:
        bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00

    if bill > 400:
        bill *= 1.15

    return max(bill, 100)

units = int(input("Enter the number of units consumed: "))
print("The total bill is Rs.", round(calculate_bill(units), 2))