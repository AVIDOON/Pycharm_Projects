sing = input()

o=0
p=0
q=0
l=0
u=0
for s in sing:
    if s.isalnum():
        o +=1
    if s.isalpha():
        p += 1
    if s.isdigit():
        q += 1
    if s.islower():
        l += 1
    if s.isupper():
        u += 1
if o >0:
    print(True)
else:
    print(False)

if p > 0:
    print(True)
else:
    print(False)

if q > 0:
    print(True)
else:
    print(False)

if l > 0:
    print(True)
else:
    print(False)

if u > 0:
    print(True)
else:
    print(False)

