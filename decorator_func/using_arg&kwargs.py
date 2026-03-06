def my_dec(func):

    def wrapper(*args,**kwargs):
        print("functions started")
        result=func(*args,**kwargs)
        print("function ended")
        return result
    return wrapper
@my_dec
def greet():
    print("hello")

greet()    

# @my_dec
# def add(a,b):
#     return a+b

# print(add(4,5))