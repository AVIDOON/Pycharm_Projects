N = int(input())
dictionary = {}
for i in range(N):
    input1 = input()
    result = input1.split()
    dictionary[result[0]] = {1: float(result[1]),2: float(result[2]),3: float(result[3])}

f_input = input()
final_dict = dictionary.get(f_input)
sum = (final_dict[1] + final_dict[2] + final_dict[3]) / 3
value = format(sum,'.2f')
print(value)