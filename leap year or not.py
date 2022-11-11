year=int(input("enter the year"))
if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0 and year%100==0:
    print("leap year")
else:
    print("not a leap year")

year=int(input("enter the year to be check"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
elif year%400==0 and year%100==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
