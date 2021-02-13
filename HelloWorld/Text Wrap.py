def wrap(string, max_width):
    a =0
    listi = ""
    for s in string:
        a += 1
        listi += s
        if a==max_width:
            listi += "\n"
            a =0
    return listi

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)