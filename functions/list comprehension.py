# #list comprehension
#
#from the list of flowers,create a new list containing flowers that have letter 'o' in it using conventional method?
# flower=["rose","jasmine","lilly","lotus","sunflower"]
# newflower=[]
# for i in flower:
#     if "o" in i:
#         newflower.append(i)
# print(newflower)

# #syntaxes of list comprehension

# # 1*********
# # newlst=[expression for i in sequence]
# #  eg:lst=[1,2,3,4,5,6]
# #     newlst=[i for i in lst]
#
# # 2***********
# # true
# # newlst=[expression for i in sequence if condtion]
# #  eg:lst=[2,3,4,5,6]
# #     newlst=[i for i in lst if i%2==0]
#
# # 3***********
# # newlst=[true expression if condition else false expression for i sequence]
# #  eg:lst=[1,2,3,4,5,6]
# #     newnum=['even' if i%2==0 else 'odd' for i in lst]

#create a list containing square of the numbers
# num=[1,2,3,4,5,6,7,8,9]
# newnum=[i*i for i in num]
# print(newnum)

#create a list containing cube of the elements?
# newnum=[i**3 for i in range(1,7)]
# print(newnum)

#create a list of even numbers?
# num=[1,2,3,4,5,6,7,8,9]
# newnum=[i for i in num if i%2==0]
# print(newnum)

#create a list that contain square of even numbers in it?
# newnum=[i*i for i in range(1,10) if i%2==0]
# print(newnum)

#create a list of odd numbers?
# newnum=[i for i in range(1,10) if i%2!=0]
# print(newnum)

#from the list of flowers,create new list having flowers with 'o' letter?
# flowers=['lilly','lotus','sunflower','rose','jasmine']
# newflowers=[i for i in flowers if 'o' in i]
# print(newflowers)

#convert all the elements in a list to uppercase letters?
# flowers=['lilly','lotus','sunflower','rose','jasmine']
# newflowers=[i.upper() for i in flowers]
# print(newflowers)

#print the same elements of a list to a new list?
# flowers=['lilly','lotus','sunflower','rose','jasmine']
# newflowers=[i for i in flowers]
# print(newflowers)

#in this list,all positions except lilly,print hibiscus?
# flowers=['lilly','lotus','sunflower','rose','jasmine']
# newflowers=['hibiscus' if i!='lilly' else 'lilly'  for i in flowers]
# print(newflowers)

#in this list,replace the sunflower and add hibiscus to that position?
# flowers=['lilly','lotus','sunflower','rose','jasmine']
# newflowers=[i if i!='sunflower' else 'hibiscus' for i in flowers]
# print(newflowers)

#from a list,print 'even' if it is an even number,otherwise print 'odd'?
# num=[1,2,3,4,5,6,7]
# newnum=['even' if i%2==0 else 'odd' for i in num]
# print(newnum)

#find all numbers from 1-1000 that are divisible by 7?
# newnum=[i for i in range(1,1001) if i%7==0]
# print(newnum)

#find all of the numbers from 1-1000 that have a 3 in them?
# newlst=[i for i in range(1,1001) if '3' in str(i) ]
# print(newlst)

#count the number of spaces in a string?
# str1=input("enter the string")
# newlst=[i for i in str1 if ' ' in i]
# print(len(newlst))

#create a list of all the consonants in the string?
# str1='yellow yaks like yelling and yawning and yesterday they yodled while eating yuky yams'
# newstr=[i for i in str1 if i not in 'a,e,i,o,u," "']
# print(newstr)

lst=[1,2,3,4,5,6,7,8,9]
newlst=[i*i if i%2!=0 else i for i in lst]
print(newlst)






















