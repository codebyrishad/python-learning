def min_value(arr):
    my_min=arr[0]

    for value in arr:
        if value < my_min:
            my_min=value
    return my_min


arr=[20,4,1,0,-1,200,45]

val=min_value(arr)
print(val)