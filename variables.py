print('hai')
#print()    builtin function
#variables=named memory locations - containers for storing data values..they are case sensitive
#identifiers=name given to variables,modules,functions,classes....

#naming rules;
#it can be of any length
#can use all letters and digits
#only _ can be use(no othr special symbols)
#cannot be start with a digit


# Multi Words Variable Names

# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascaseal C
# Each word starts with a capital letter:
# MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"


#keywords=having special meaning or purposes
#eg;if,else,break,while,continue,pass...


a=4
b=7
print(a)
print(b)

a,b=4,7
print(a)
print(b)

a=b=5
print(a)
print(b)


#Global Variables

#Variables that are created outside of a function  are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

#Example
#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.

#Example
#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#The global Keyword

#Normally, when you create a variable inside a function, that variable is local,
# and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

#Example
#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Also, use the global keyword if you want to change a global variable inside a function.

#Example
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)