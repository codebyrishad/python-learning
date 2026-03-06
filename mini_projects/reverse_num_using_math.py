
# while number > 0
# last_digit = number % 10
# number = number // 10

def rev_number(number):
    sign= -1 if number < 0 else 1
    number=abs(number) 
    reversed_number=0
    while number > 0 or number < 0:
        last_digit=number%10 
        reversed_number=reversed_number*10+last_digit
        number=number//10
    return sign*reversed_number
number=-1234
print(rev_number(number))
