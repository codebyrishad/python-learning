new_list=[1,2,3,4,5]

count=0
for item in new_list:
    count=count+1

print(count)    




# my_list=len(new_list)
# print(my_list)



"Using while_loop"

numbers = [10, 20, 30, 40, 50]

count = 0

index=0

while True:
    try:
        numbers[index]
        count=count+1
        index=index+1
    except IndexError:
        break
print(count)        