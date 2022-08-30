#map function
#syntax:
#map(function,sequence)

# def mul(n):
#     return n*n
# num=[1,2,3,4,5]
# result=map(mul,num)
# print(list(result))

# num=[1,2,3,4]
# result=map(lambda n:n*n,num)
# print(list(result))
#
# num1=[1,2,3,4,5,6]
# num2=[7,8,9,10,11,12]
# result=map(lambda x,y:x+y,num1,num2)
# print(list(result))
#
# fruits=['apple','orange','mango','banana','jackfruit']
# result=map(len,fruits)
# print(list(result))
#
# fruits=['apple','orange','mango','banana','jackfruit']
# result=map(list,fruits)
# print(list(result))

# Write a Python program to triple all numbers of a given list of integers. Use Python map
# triple=input("enter the elements").split()
# lst1=map(int,triple)
# result=map(lambda x:x*3,lst1)
# print(list(result))

# Write a Python program to add three given lists using Python map and lambda
# lst1=input("enter the list1 elements").split()
# lst2=input("enter the list2 elements").split()
# lst3=input("enter the list3 elements").split()
# print("\nfirst list:",lst1)
# print("\nsecond list:",lst2)
# print("\nthird list:",lst3)
# first=map(int,lst1)
# second=map(int,lst2)
# third=map(int,lst3)
# result=map(lambda x,y,z:x+y+z,first,second,third)
# print("\nnew list after adding 3 lists:")
# print(list(result))

#Write a Python program to create a list containing the power of said number in bases raised to the corresponding number
# in the index using Python map
# base_number=[1,2,3,4,5]
# index=[1,2,3,4,5]
# result=map(lambda x,y:x**y,base_number,index)
# print(list(result))

#Write a Python program to square the elements of a list using map() function
# lst=input("enter the list elements").split()
# lst1=map(int,lst)
# result=map(lambda x:x*x,lst1)
# print(list(result))

#Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from
# a given sequence. Use map() function
# str=input("enter the string")
# result=map(str.swapcase(),str)
# print(list(str(result)))

# def change_cases(s):
#     return str(s).upper(), str(s).lower()
#
# chrars = {'a', 'b', 'E', 'f', 'a', 'o', 'b', 'O', 'i', 'o', 'U', 'a'}
# print("Original Characters:\n", chrars)
#
# result = map(change_cases, chrars)
# print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
# print(set(result))

# Write a Python program to add two given lists and find the difference between lists. Use map() function
# def addition_subtrction(x, y):
#     return x + y, x - y
# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]
# print("Original lists:")
# print(nums1)
# print(nums2)
# result = map(addition_subtrction, nums1, nums2)
# print("\nResult:")
# print(list(result))

lst=[15,3,6,8,9]
newlst=map(lambda x:x*x,lst)
print(list(newlst))











