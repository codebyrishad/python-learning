# ✅ Question 2 – Even or Odd
# Requirements:
# Take number from user
# Use try/except
# Print:
# "Even"
# "Odd"
# Handle invalid input properly

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

except ValueError:
    print("Enter a valid number")
        
        