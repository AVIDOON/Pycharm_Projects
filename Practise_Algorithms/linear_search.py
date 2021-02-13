# A = [23, 22, 11, 19, 7, 33]


A = [23, 22, 11, 19, 7, 33, 22]
a = int(input("Enter the number you want to search: "))
size = len(A)
index = []
for i in range(size):
    if a == A[i]:
       index.append(i)

if len(index) == 0:
    print(str(a) + " is not found.")
else:
    print(str(a) + " is found at ",end="")
    for i in range(len(index)):
        if i < len(index):
          print(str(index[i] +1), end=',')


