


# 24 12 34 8 11 6

array = [24, 34, 8, 11, 6, 29]
print("Unsorted array")
print(array)

size = len(array)

for i in range(size - 1):
    min_index = i
    for j in range(i+1,size):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]



print ("Sorted array")

print(array)

