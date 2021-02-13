string = "ABCDCDC"
substring = "CDC"
str_len = len(string)
sub_len = len(substring)

# logic
# match one by one and find the first letter of substring

for i in range(sub_len):
    for j in range(str_len):
        if substring[i] == string[j]:
            print(str(i) + "and" + str(j))