def sq(n):
    for i in range(1,n+1):
        yield i*i

for num in sq(5):
    print(num)