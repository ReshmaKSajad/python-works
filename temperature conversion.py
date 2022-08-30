
print("1.celcius to farenheit")
print("2.farenheit to celcius")
ch=int(input("enter your choice"))
if ch==1:
    c=float(input('enter the temperature in celcius scale'))
    f=9/5*c+32
    print("temperature in farenheit scale=",round(f,2))
elif ch==2:
    f=float(input("enter the temperature in farenheit scale"))
    c=(f-32)*5/9
    print("temperature in celcius scale=",round(c,2))
else:
    print("wrong choice")

