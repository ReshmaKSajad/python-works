# Python code to demonstrate working of Uppercase Half String
# Using upper() + loop + len()

str="reshma"
print("The original string is :",str)
hlf_idx=len(str)//2
result=" "
for i in range(len(str)):
    if i>= hlf_idx:
        result+=str[i].upper()
    else:
        result+=str[i]
print("The resultant string :",result)
