user_input = int(input())
for spaces in range(user_input,-1,-1):
     line = ''
     line += 's' * spaces
     for stars in range(3,spaces,-1):
      line += '#'
     print(line)