i = 0
j = 0
count = 0
temp = 0
string = "ABCDACDA"
sub = "CDA"
while j < len(sub):
    while i < len(sub):
        if sub[j] != string[i]:
            i += 1
            temp = i
        else:
            j += 1
            i = temp
    if j == len(sub) - 1:
        count += 1
print(count)
