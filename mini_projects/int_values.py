# write a program that:
# Prints whether it is:
# Takes a number from user
# Positive
# Negative
# Zero
# also decimal values

while True:
            try:
                number=float(input("enter a number"))

                if number > 0:
                    print(number,": is a positive number ")
                elif number < 0:
                    print(number,": is negative number")
                else:
                    print("its zero")
                break
            except ValueError:
                print("only number is supported")    

