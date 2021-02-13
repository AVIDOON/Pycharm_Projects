# This isn't an optimized way of bubble sort since it takes O(n^2)

# [11, 8, 4, 1, 12]
# 8 11 4 1 12
# 8 4 11 1 12
# 8 4 1 11 12


array = [64, 34, 25, 12, 22, 11, 90]
size = len(array)
no_of_swaps = 0

for i in range(size):

 # size - i -1 because each time last element is already sorted
  for j in range(size - i - 1):
     if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        no_of_swaps += 1


print(array)
print(no_of_swaps)


