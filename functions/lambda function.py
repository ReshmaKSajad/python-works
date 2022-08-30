#lambda function- also called anonymous function
#syntax-
#lambda arg1,arg2,....:expression
# sq=lambda n:n*n
# print("square is",sq(5))
# sum=lambda a,b:a+b
# print("sum is",sum(5,8))
# sum=lambda p,q,r:p+q+r
# print("sum is",sum(3,4,5))
# cube=lambda n:n*n*n
# print("cube is",cube(3))

def sum(n1,n2):
    c=n1+n2
    print("sum of the numbers=",c)
sum(6,8)