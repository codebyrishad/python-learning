list = [10, 20, 30, 40, 50]
n=3

new_list=[]


for i in range(len(list)):
    if i != n :
        new_list.append(list[i])

print(new_list)        