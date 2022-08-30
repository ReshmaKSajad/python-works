#armstrong number: number whose sum of cube of the digits will alternately gives the same number
#eg: 153= 1**3 + 5**3 + 3**3 = 1+125+27 = 153

n=int(input("enter the number"))  #153
sum=0
num=n
while n>0:
    d=n%10         #d = 153%10 = 3       d = 15%10 = 5         d = 1%10 = 1
    sum=sum+d**3   #sum = 0+3**3 = 27   sum = 27+125 =152    sum = 152 + 1= 153
    n=n//10        #n = 153//10 = 15     n = 15//10 = 1       n = 1//10 = 0
print(sum)
if num==sum:
    print("armstrong")
else:
    print("not armstrong")