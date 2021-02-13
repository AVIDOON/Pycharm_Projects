inp = int(input())
for i in range(0,inp):
    a,b = input().split()

    try:
        c = int(a)/int(b)
        print(int(c))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

