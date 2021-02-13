abc = [
    [2, 0, 0, 1],
    [1, 2, 0, 4],
    [0, 3, 1, 6],
    [0, 0, 6, 4]
]
output = 18

print(abc)

# 00, '10' then 01, 20 then '11', '21' then 12 , 31 then '22', '32' then 23, '33'
N = 4
i = 0; j = 0
sums = abc[i][j]
while i < N or j < N:
    if i + 1 <= N:
        if abc[i+1][j] is not 0:
            sums += abc[i+1][j]
        else:
            sums += abc[i+1][j+1]
