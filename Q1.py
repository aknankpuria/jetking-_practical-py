#In Python Programming, how many types of errors are possible and define them.

#1 syntax error
    #syntax error occurs when the code is not in proper format.

from math import factorial
x=15

if x==15
    print("x is 15")

# in upper code there is syntax error because we have not use : in if statement.

if x==15:
    print("x is 15")    

    #now this is error free
    

#2 run time error also known as exception error
    #run time error occurs when the program is not able to run the code.

def div(a,b):
    print(a/b)

div(16,2) #it will now throw error because we have not given any wrong values

div(16,0) #it will now throw error because we have given 0 as value of b

#3 logical error
  



def calc_factorial(n):
    if n==0:
        return 1
    else:
        return n*calc_factorial(n-1)*2  # here we have done logical error program will execute perfectly but it wont give desired result.
    
print(calc_factorial(5))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#4 type error

x=5
y = "6"
print ( x+y)
#type error because we cant add string to integer.

#5 index error

mylist = [1,2,3]

print(mylist[3])

#index error because there is no index 3 in list. we have max index 2.

#6 key error

mydict = {1:"one",2:"two"}

print(mydict[3])

#key error because there is no key 3 in dictionary. we have only 2 keys.
