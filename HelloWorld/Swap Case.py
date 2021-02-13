def swap_case(s):
    a1 = ''
    for i in s:
        if i.isupper():
            a1 += i.lower()
        elif i.islower():
            a1 += i.upper()
        else:
            a1 += i

    return a1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)