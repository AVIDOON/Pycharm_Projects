# Factorial of a number
# fact = 1
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# print(factorial(5))

# LCM of a number

a = int(input("Enter first number"))
b = int(input("Enter second number"))

# 4,8
# 2-> 2,4
# 2-> 1,2

list1 = []
for i in range(2,a):
    if a % i == 0 and b % i == 0:
        list1.append(i)

print(list1)