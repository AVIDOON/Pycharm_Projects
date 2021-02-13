sum = 0
n = int(input("Enter a number"))
x = 100
while n != 0:
    a = n % 10
    sum += x * a
    x = x/10
    n = int(n/10)

print(int(sum))
