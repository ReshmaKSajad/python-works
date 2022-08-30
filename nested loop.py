#nested loop

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# n=int(input("enter the number"))
# for i in range(n):
#     for j in range(8):
#         print("$",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()