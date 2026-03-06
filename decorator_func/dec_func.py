# Start–End Printer (Basic Decorator)

def my_dec(func):
 
    def wrapper():
        print("functions  started")
        func()
        print("functions  ended")
    return wrapper

@my_dec
def greet():
    print("hello")

greet()