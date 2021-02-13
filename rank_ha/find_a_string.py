def count_substring(string, sub_string):
    lenth = len(sub_string)
    i = 0
    count = 0
    for s in range(0,len(string)):
        if string[s] == sub_string[0]:
            state = s + 1



    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)