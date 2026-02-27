def reversed_str(my_list):
    new_list=[]

    for x in my_list:
        new_list=[x] + new_list

    return new_list


my_list=[1, 2, 3, 4]


val=reversed_str(my_list)
print(val)
