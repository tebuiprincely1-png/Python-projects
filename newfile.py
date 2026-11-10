# Multiplication and Division Table

number = float(input("Enter a number: "))
limit = int(input("Enter the table limit: "))

print("\nMULTIPLICATION TABLE")
print("-------------------------")

for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

print("\nDIVISION TABLE")
print("-------------------------")

for i in range(1, limit + 1):
    result = number / i
    print(f"{number} / {i} = {result:.2f}")
()