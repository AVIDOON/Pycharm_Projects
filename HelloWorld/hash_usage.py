length = int(input())
values = [int(x)for x in input().split()]
tup = tuple(values)
print(hash(tup))

