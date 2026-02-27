new=[3,2,4,6,5,7,8,9]

for i in range(len(new)-1):
    for j in range(len(new)-1):
        if new[j]> new[j+1]:
            temp=new[j]
            new[j]=new[j+1]
            new[j+1]=temp

print(new)        


# new.sort()
# print(new)