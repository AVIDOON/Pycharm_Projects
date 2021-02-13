import math
def prime_no(n):
    flag = 0
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            flag = 1
    if n==1:
        print("No")
    elif(flag):
        print("No")
    else:
        print("Yes")

def factors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (n / i == i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2

    prime_no(cnt)

if __name__ == '__main__':
     T = int(input())
     for i in range(1,T+1):
        inp = int(input())
        factors(inp)


