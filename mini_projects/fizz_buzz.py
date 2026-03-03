# Print numbers from 1 to 100.

# Rules:
# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If divisible by both → print "FizzBuzz"
# Otherwise → print number
# ⚠ Important: Order of conditions matters.
# Now improve FizzBuzz:
# Print numbers from 1 to 100
# But count how many times:
# Fizz appeared
# Buzz appeared
# FizzBuzz appeared
# Print the counts at the end

count_fizz=0
count_buzz=0
count_fizbuzz=0

for i in range(1,101):

    if i%3==0 and i%5==0:
        print("fizz_buzz")
        count_fizbuzz+=1
    elif i % 3 == 0:
        print("fizz")
        count_fizz += 1
    elif i % 5 == 0:
        print("buzz")
        count_buzz += 1
    else:
        print(i)

print("\nCounts:")
print("Fizz:", count_fizz)
print("Buzz:", count_buzz)
print("FizzBuzz:", count_fizbuzz)