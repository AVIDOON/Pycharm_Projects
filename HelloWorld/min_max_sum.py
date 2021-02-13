input1 = input()
result = input1.split()
list1 = []
sum = 0

for i in result:
    sum = sum + int(i)

for j in range(0,5):
    list1.append(sum - int(result[j]))

list1.sort()

print(list1[0],end= ' ')
print(list1[4])