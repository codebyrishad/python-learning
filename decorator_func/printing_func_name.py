def func_namer(func):

    def wrapper(*args,**kwargs):
        print("running function:",func.__name__)
        func(*args,**kwargs)

    return wrapper
@func_namer
def greet():
    print("hello")    

greet()