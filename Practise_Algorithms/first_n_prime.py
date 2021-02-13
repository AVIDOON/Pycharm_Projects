def print_prime(upto):
    flag = 0
    for i in range(upto):
        num = i*5  # 2 3 5 7 11
        for j in range(1,num):
            if num % j == 0:
                flag += 1
        if flag == 1:
             print(i)



n = int(input("Enter the number you want upto? "))
print_prime(n)


# num = int(input("Enter a number"))
# flag = 0
# for i in range(1,int(num/2)+1):
#     if num % i == 0:
#         flag += 1
#
# if flag == 1:
#     print("prime")
# else:
#     print("non-prime")
