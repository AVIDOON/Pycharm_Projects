inp = int(input())
list1 = [int(x) for x in input().split()]
list1.sort()
print(list1.count(list1[inp - 1]))