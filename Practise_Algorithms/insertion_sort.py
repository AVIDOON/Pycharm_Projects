

array = [12, 9, 11, 5, 6]

size = len(array)

for i in range(1,size):
    for j in range(i):
       if array[j] > array[i]:
         array[i], array[j] = array[j], array[i]
       print(array)

print('Sorted Array : ')
print(array)