#variable length arguement -   we can add any number of arguements to the function - non keyword arguement
def fun1(*args):
    #print(type(args))
    s = 0
    for i in args:
       # print(i)
        s += i
    return s
print("call 1")
res = fun1(1,2,3,4,5,6,7,8,9)
print(res)
print("call 2")
print(fun1(10,11,12,13,14,15,16,17,18))



def var_length(*args):
    print(type(args))
    for i in args:
        print(i)
var_length(1,2,3,4,5)
var_length(4,7,8,9,3)