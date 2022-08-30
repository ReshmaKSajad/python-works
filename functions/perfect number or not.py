def perfect(num):
    s=0
    for i in range(1,num,1):
        if num%i==0:
            s=s+i
    print("sum is",s)
    if s==num:
        print("perfect number")
    else:
        print("not perfect")
perfect(6)
