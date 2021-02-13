def print_formatted(number):
    for i in range(1, number + 1):
        print(i, octal_number(i), hexadecimal_number(i), binary_number(i))


def binary_number(inp):
    binary = 0
    i = 1
    j = 0
    while inp != 0:
        rem = inp % 2
        binary += rem * i
        inp = int(inp / 2)
        i = i * 10
        j += 1
    return binary


def octal_number(inp):
    octal = 0
    i = 1
    j = 0
    while inp != 0:
        rem = inp % 8
        octal += rem * i
        inp = int(inp / 8)
        i = i * 10
        j += 1

    return octal


def hexadecimal_number(inp):
    hexadecimal = ''
    i = 1
    j = 0
    while inp != 0:
        rem = inp % 16
        if rem == 10:
            rem = 'A'
        elif rem == 11:
            rem = 'B'
        elif rem == 12:
            rem = 'C'
        elif rem == 13:
            rem = 'D'
        elif rem == 14:
            rem = 'E'
        elif rem == 15:
            rem = 'F'
        else:
            rem = str(rem)

        hexadecimal += rem
        inp = int(inp / 16)
        i = i * 10
        j += 1
    return hexadecimal[::-1]


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
