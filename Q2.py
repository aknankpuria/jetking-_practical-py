#What is an Exception and write the syntax of exception handling?

#Exception is an event that occurs when an error occurs in the program during runtime .

#Syntax of Exception Handling :

# try:
      #  statements

# except Exception:
   #  statements

#example

try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=a/b
    print(c)    

except Exception as e:
    print(e)
