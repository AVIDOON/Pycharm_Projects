# Method 1

inp = input("Enter the string : ")
list1 = []
for i in inp:
    count = 0
    for j in inp:
        if i == j:
            count += 1
    if i not in list1:
      print("Number of ", i, "is : ", count)
    if i not in list1:
     list1.append(i)

#   Time complexity is O(n2)
#   Space complexity is O(n)

# Method 2

inp = input("Enter the string : ")
list1 = []
for i in inp:
    count = 0
    for j in inp:
        if ord(i) == ord(j):
            count += 1
    if i not in list1:
      print("Number of ", i, "is : ", count)
    if i not in list1:
     list1.append(i)

#   Time complexity is O(n2)
#   Space complexity is O(n)

# Method 3

import re
list1 = []
inp = input("Enter the string : ")
for i in inp:
    x = len(re.findall(i,inp))
    if i not in list1:
      print("Number of ", i, "is : ", x)
    if i not in list1:
      list1.append(i)

#   Time complexity is O(n)
#   Space complexity is O(n)


# Method 4
inp = input("Enter the string : ")
list1 = []
for i in inp:
    x = inp.count(i)
    if i not in list1:
      print("Number of ", i, "is : ", x)
    if i not in list1:
      list1.append(i)

#   Time complexity is O(n)
#   Space complexity is O(n)
