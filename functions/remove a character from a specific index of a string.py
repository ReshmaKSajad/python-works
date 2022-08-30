#remove a character from a specific index of a string?

str = input("enter the string")
index = int(input("enter the index"))
new_str = str[:index-1] + str[index:]
print("string after removing the specific index =",new_str)


#find the nth power of a number using recursion?
def power(n,p):
    if p == 0:
        return 1
    return n * power(n,p-1)
n = 5
p = 2
print("power is",power(n,p))

