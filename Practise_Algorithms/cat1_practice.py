# Finding Maximum in a list

# Method1
#
# list1 = [20, 15, 11, 25, 6, 13]
# list1.sort()
# print(list1[-1])
#
#
# # Method2
# list1 = [20, 15, 11, 25, 6, 13]
# print(max(list1))
#
# # Method3
# list1 = [20, 15, 11, 25, 6, 13]
# max = list1[0]
# for num in list1:
#     if max < num:
#         max = num
# print(max)

# Finding maximum using recursion function
# def maximum(List1):
#     if len(List1) == 1:
#         return List1[0]
#     else:
#         return max(List1[0],maximum(List1[1:]))
#
# List1= [2,4,6,23,1,46]
# print(maximum(List1))


# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#     # Driver Program
#
#
# print(fibonacci(9))

# import time
# import webbrowser
#
# breaks = 3
# count = 1
# current = time.ctime()
# print(current)
#
# while(count<= breaks):
#     time.sleep(5)
#     webbrowser.open("https://play.typeracer.com")
#     count +=1

# # Fabonicci series
# def fab(inp):
#     first = 0
#     second = 1
#     print(first)
#     print(second)
#     i = 0
#     for i in range(inp - 2):
#         sum = first + second
#         print(sum)
#         first = second
#         second = sum
# fab(10)

# import os
#
#
# def rename_files():
#     file_list = os.listdir("/Users/avinashraj/Documents/prank")
#     print(file_list)
#     saved_path = os.getcwd()
#     print(saved_path)
#     os.chdir("/Users/avinashraj/Desktop/prank copy")
#     changed_path = os.getcwd()
#     print(changed_path)
#
#     for file_name in file_list:
#         os.rename(file_name, file_name.strip("0123456789"))
#
#     os.chdir(saved_path)
#
#
# rename_files()

# Finding unique no in the list
# list1 = [1, 2, 1, 3, 2, 4, 5]
# list2 = []
#
# for x in list1:
#     if x not in list2:
#         list2.append(x)
# print(list2)


# # Sum Triplet of a number
#
# list1 = []
# def triplet_no(n):
#     for a in range(10):
#         for b in range(10):
#             for c in range(10):
#                 if a + b + c == n:
#                    list1.append(c)
#                    list1.append(b)
#                    list1.append(a)
#                    print(list1,end = ", ")
#                    list1.clear()
#
# triplet_no(15)

# Substring of a string
# def subString(s, n):
#     for i in range(n):
#         for len in range(i + 1, n + 1):
#             print(s[i: len])
#
# s = "abcd"
# subString(s, len(s))

# # Addition of matrix
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X)):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)

#
# # Addition of matrix
# X = [[12, 7, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# for i in range(len(X)):
#    for j in range(len(X[0])):
#        for k in range(len(X[]))
#        result[i][j] = X[i][j] * Y[i][j]
# for r in result:
#    print(r)
