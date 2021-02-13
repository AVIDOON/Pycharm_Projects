def char_to_no(arg):
    switcher = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,

    }
    return  switcher.get(arg,'Invalid')

def no_to_char(arg):
    switcher = {
        0 : 'a',
        1 : 'b',
        2 : 'c',
        3 : 'd',
        4 : 'e',
        5 : 'f',
        6 : 'g',
        7: 'h',
        8: 'i',
        9: 'j',
        10: 'k',
        11: 'l',
        12: 'm',
        13: 'n',
        14: 'o',
        15: 'p',
        16: 'q',
        17: 'r',
        18: 's',
        19: 't',
        20: 'u',
        21: 'v',
        22: 'w',
        23: 'x',
        24: 'y',
        25: 'z',

    }
    return  switcher.get(arg,'Invalid')

def cipher_fun(list1):
    for i in range(16):
        v1 = (list1[0] - i) % 26
        for j in range(16):
            v2 = (list1[1] - j) % 26
            for k in range(16):
                v3 = (list1[2] - k) % 26
                for l in range(16):
                    v4 = (list1[3] - l) % 26
                    for m in range(16):
                       v5 = (list1[4] - m) % 26
                       print(no_to_char(v1)+no_to_char(v2)+no_to_char(v3)+no_to_char(v4)+no_to_char(v5))
#
if __name__ == '__main__':
    inp = input()
    list1 = []
    for i in inp:
        list1.append(char_to_no(i))

    cipher_fun(list1)


