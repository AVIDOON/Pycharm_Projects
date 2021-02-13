#  demerit of this code is that it has not added two whitespaces inplaces
#  of two rather it has added only one.
import re
def solve(input):
    # inp = input.split()
    # lent = len(inp)
    new_string = ""
    act_string = ""
    # x = re.search("\s",input)
    # print(x.start())

    new_input = input.replace(input[0],input[0].upper(),1)
    x = re.search("\s", input)
    print(x.start() + 1)

    # for i in range(lent):
    #     new_string += inp[i].capitalize() + " "
    #     act_string = new_string.rstrip()

    return new_input


input = input("Enter your name")
solved = solve(input)


print(solved)


