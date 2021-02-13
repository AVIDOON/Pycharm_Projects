N = int(input())
list1 = []
i=0
while i < N:
    result = [int(x) for x in input().split()]
    if result[0] == 'insert':
     list1.insert(int(result[1]), int(result[2]))
    if result[0] == 'print':
     print(list1)
    if result[0] == 'remove':
     list1.remove(int(result[1]))
    if result[0] == 'append':
     list1.append(int(result[1]))
    if result[0] == 'sort':
     list = sorted(list1)
     list1 = list
    if result[0] == 'pop':
     list1.pop()
    if result[0] == 'reverse':
     list1.reverse()
    i += 1




