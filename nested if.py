#nested if
#if statement contain another if statement
#syntax of nested if:

#1.if condition1:               this is type 1 of nested if
#     if condition2:
#            statements
#  else:
#      statements

#     *************************
# 2.if condition:               this is type 2 of nested if
#      statements
#  else:
#      if condition:
#            statements
#      else:
#            statements
#
#    ***************************
#3.if condition:                   this is type 3 of nested if
#      if condition:
#           statements
#      else:
#           statements
#  else:
#      if condition:
#           statements
#      else:
#           statements

#check the given number is positive ,negative ,zero?

n=int(input("enter the number"))
if n>0:
    print("positive number")
else:
    if n<0:
        print("negative number")
    else:
        print("zero")
