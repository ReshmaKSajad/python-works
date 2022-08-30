def add(a, b):
    # returning sum of a and b
    return a + b


def is_true(a):
    # returning boolean of a
    return bool(a)


# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))

res = is_true(2 < 5)
print("\nResult of is_true function is {}".format(res))
#In Python, the new line character “\n” is used to create a new line. When inserted in a string all the characters
# after the character are added to a new line. Essentially the occurrence of the “\n” indicates that the line ends
# here and the remaining characters would be displayed in a new line.