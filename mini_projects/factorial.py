# Write a program that:
# Takes a number n
# Prints factorial of n
# Use loop
# Handle invalid input
# Handle negative numbers properly

while True:
    try:
            n=int(input("enter a number"))

            if n < 0:
                print("Factorial is not defined for negative numbers")
                break
            result=1
            for i in range(1,n+1):
                 result=result*i    
            
            print(f"{n}! = {result}")


    except ValueError:
         print("please enter a valid integer")  
