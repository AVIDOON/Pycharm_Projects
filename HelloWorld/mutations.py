string = input()
list1 = list(string)
input1 = input().split()
list1[int(input1[0])] = input1[1]
new_string = ''.join(list1)
print(new_string)