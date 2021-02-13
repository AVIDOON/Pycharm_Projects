no_of_input = int(input())

list_Value = []

for i in range(no_of_input):
    list1 = []
    list1.append(input())
    list1.append(float(input()))
    list_Value.append(list1)
print(list_Value)

list_Value.sort()

print(list_Value)
marks_list = []
name_list = []
for i in range(no_of_input):
    for j in range(1,2):
        marks_list.append(list_Value[i][j])

for i in range(no_of_input):
    for j in range(1):
        name_list.append(list_Value[i][j])

marks_list.sort()
print(marks_list)

print(marks_list)
print(name_list)