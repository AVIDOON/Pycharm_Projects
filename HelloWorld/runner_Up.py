num_of_input = int(input())

list_value = [int(x) for x in input().split()]

list_value.sort()

maximum = list_value[0]
for index_value in list_value:
    if maximum < index_value:
        maximum = index_value

if maximum == list_value[0]:
    second_max = list_value[1]
else:
    second_max = list_value[0]

for index_value in range(1,len(list_value)-1):
     if second_max < list_value[index_value] and list_value[index_value] != maximum:
        second_max = list_value[index_value]


print(second_max)

