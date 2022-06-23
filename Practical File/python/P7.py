i = float(input("\n\tEnter Divisor: "))
j = float(input("\n\tEnter Divident: "))

try:
    print(f"\n\tThe Quotient after division is : {i/j}")

except ZeroDivisionError:
    print("\n\tDiviion by Zero detected")



    