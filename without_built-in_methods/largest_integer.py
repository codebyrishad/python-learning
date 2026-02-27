def max_value(arr):
    my_max=arr[0]
    for x in arr:
        if x > my_max:
            my_max=x  
    return my_max

arr=[20,4,1,200,45]

print(arr)

large=max_value(arr)
print(large)