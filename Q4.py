#  Write a Python Program to demonstrate how a user can
# customize the exceptions using User-Defined Exceptions.



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
    #print(e.age)  
