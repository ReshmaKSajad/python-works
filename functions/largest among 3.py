#using function,find the largest among 3 numbers
def largest_among_3(a,b,c):
    if a>b and a>c:
        print(a,"is largest")
    elif b>a and b>c:
        print(b,"is largest")
    elif c>a and c>b:
        print(c,"is largest")
    else:
        print("two or all numbers are equal")
largest_among_3(2,3,4)
        