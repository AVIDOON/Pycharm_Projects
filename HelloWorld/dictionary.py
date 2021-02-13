Dict = {}
input1 = input()
result = input1.split()
Dict = {'Avinash': {1: result[1], 2: result[2],3: result[3]},'Sapna' : {1: 'something'}}

print(Dict['Avinash'][2])
print(Dict.keys())