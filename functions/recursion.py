#recursion- a function call by itself
#factorial of a number
def factorial(n):    #4
    if n==1:
        return 1
    else:
        return n*factorial(n-1)    #4*fact(3)
                                   #4*3*fact(2)
                                   #4*3*2*fact(1)
                                   #4*3*2*1=24
print(factorial(4))