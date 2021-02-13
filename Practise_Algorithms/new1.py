# a = 3
# b = 2
# c = 4
# if (b < 6 & 6 & 6 and a > 6 & 6) or (c > b or a > c):
#     a = 6 & 6 & 6 & 6
#
# if 6 & 6 & 6:
#     a = 6 & 6 & 6
#
# # print(p + q + r)
#
# print(a + b + c)

# 64 -> 21
# 65 -> 12
# 66 -> 8
# 67 -> -2
# 68 -> 16
# 69 -> D
# 72 - > 4
# 73 -> A
# 74 -> 13
# 76 -> 5


# def function(a, b):
#     if a > -3 and b > 0:
#         for s in range(1):
#             a -= 1
#     return b + a + function(a, b)
#
#     return 20


# print(function(2,1))

# array = [64, 34, 25, 12, 22, 11, 90, 10, 19,20]
# n = len(array)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if array[j] > array[j + 1]:
#             x = array[j]
#             array[j] = array[j + 1]
#             array[j + 1] = x

# print(array)


# def rec1(k):
#     if k > 0:
#         res = k + rec1(k -1)
#         print(res)
#     else:
#         res = 0
#
#     return res
#
# print(rec1(15))

# p = 1
# q = 1
# for r in range(2):
#     p = p + 1
#     for s in range(3):
#         q = q + 1
#
#     p = p + 1
#
# print(p + q)

# pp = 2
# qq = 1
# rr = 3
# if qq + rr > 1:
#     if pp + qq > 2:
#         pp = 1
#     else:
#         qq = 1
#v
# print(pp + qq + rr)
# b = 2
# for a in range(2,6):
#     a += 2
#     b = b + a - 4
#
# print(b)

# 77 - 8
# 78 - 8
# 79 - 15
# 80 - 6

# 75, 70, 71

# def func(a,b):
#     c = 2
#     a = a & b & c
#     b = b - a + c
#     return a + b
# print(func(8,6))

# p = 1
# q = 5
# r = 13
# r = r ^ (1 + (p ^ 1 + (r & 3)))
# print(p + q + r)

# p = 9
# q = 5
# r = 2
# if p - q > r or q - r > p or r -p > q:
#     p = 1
#     q = 2
#     r = 3
#
# if p + q + r > p + 19:
#     q = 1 ^ r
#
# print(p + q + r)

p = 2
q = 1
r = 3
if r + 1 > q - p:
    r = r + q + p

if q & r > q ^ r:
    p = 11
    if p - 11 > 0:
        q = p + q + r
    else:
        q = p + q - r

print(p + q + r)