#check the given number is armstrong number or not?
n = int(input("enter the number"))
count = 0
num = num1 = n
sum = 0
while n > 0:
    n = n // 10
    count = count +  1
print("number of digits=",count)
while num > 0:
    d = num % 10
    sum = sum + pow(d,count)
    num = num // 10
if num1 == sum:
    print("armstrong")
else:
    print("not armstrong")
