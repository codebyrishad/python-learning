def even(n):
    for i in range(1,n+1):
        if n%2==0:
            yield i


for num in even(10):
    print(num)