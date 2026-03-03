# Take 3 numbers from user
# Use try/except
# Do NOT use max()
# Print the largest number
# Clean formatting
# No unnecessary logic



while True:
            try: 
                num1=int(input("enter num1 : "))
                num2=int(input("enter num2 : "))
                num3=int(input("enter num3 : "))
                break
              
            except ValueError:
                    print("enter a valid number") 

largest=num1 
if num2 > largest:
        largest=num2
if num3 > largest:
    largest=num3           
print(f"{largest} is the largest number")    
  