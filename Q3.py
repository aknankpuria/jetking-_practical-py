# Define User-Defined Exceptions in Python Programming.
  #we create own exceptions using the class Exception. it is created to force certain constraints like voting age etc.


#  syntax:

# class ExceptionName(Exception):
    # pass  


class AgeTooSmallError(Exception):
    def __init__(self, age):
        # self.age = age
        print("Age is too small")

try: 
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError(age)
    else:
        print("You are eligible")
    
except AgeTooSmallError as e:
    print(e)    
