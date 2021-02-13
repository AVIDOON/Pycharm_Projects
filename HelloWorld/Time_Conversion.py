inp = input()
result = inp.split(':')
actual_Time = '00:00:00'
if int(result[0])== 12 and result[2].__contains__('AM'):
    actual_Time = '00' + ":"+result[1]+":" + result[2].replace('AM','')

if int(result[0])== 12 and result[2].__contains__('PM'):
    actual_Time = inp.replace('PM','')

if int(result[0])>= 1 and int(result[0])<12 and result[2].__contains__('PM'):
     newTime = str(int(result[0]) + 12)
     second = result[2].replace('PM','')
     actual_Time = newTime + ':' + result[1] + ":" + second

if int(result[0])>= 1 and int(result[0])<12 and result[2].__contains__('AM'):
    actual_Time = inp.replace('AM', '')


print(actual_Time)
