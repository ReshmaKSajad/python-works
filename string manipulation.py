#string manipulation
str="python"
#indexing:
#str[0]="p",str[1]="y",str[2]="t".....
#forward indexing                starts with 0 and the 0th value is the first letter
#print("str[0]=",str[0])
#print("str[1]=",str[1])
#print("str[5]=",str[5])
#backward indexing               starts with -1 and the -1th value is the last letter
#n=-1, o=-2 ,h=-3, t=-4....
#print(str[-1])
#print(str[-2])
#print(str[-5])
#slicing
print(str[0:4])
#if the end value is not specified,the value after the first value will print
#if the starting value is not specified,it will start with 0
print(str[2:])
print(str[:6])
print(str[1:5])
print(str[-5:-1])
#if starting value and ending value is not specified, then it will start with 0 and end by the last letter
print(str[:])
#if step is also given,then it will also print as step wise
print(str[::2])
print(str[0:6:3])
print(str[::-1])
