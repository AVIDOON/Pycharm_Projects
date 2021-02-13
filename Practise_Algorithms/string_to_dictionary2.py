import  json

def make_string():
    dict = {}
    for i in range(1):
     inp = input("Enter input ")
     out = input('Enter output')
     if(out.__contains__(";")):
         out = out.split(';')
         # print(out)
     dict[inp] = out
    print(dict)
    # {'~00P003RATA8': ['~00D064230', '500', '230', '500', '1000', '0900', '', '080', '280', '090', '080', '280', '270', '0', '024', '400', '700']}
    # print(dict['AVINASH'][1])

# working with frequency, voltage and powersupply
# data_dict = {}
# new_dict =  {'~00P003RATA8': ['~00D064230', '500', '230', '500', '1000', '0900', '', '080', '280', '090', '080', '280', '270', '0', '024', '400', '700']}
# a = new_dict['~00P003RATA8'][1]
# _a = int(a)/10
# print(type(_a))
# data_dict["freq (in Hz)"] = _a
# print(_a)
#
# b = new_dict['~00P003RATA8'][2]
# _b = int(b)
# print(type(_b))
# data_dict["Voltage (in Volts)"] = _b
# print(_b)
#
# c = new_dict['~00P003RATA8'][5]
# _c = int(c)/100
# print(type(_c))
# data_dict["Power supply (in KWs)"] = _c
# print(_c)
#
# print(data_dict)


    ini_string = json.dumps(dict)
    print("initial 1st dictionary", ini_string)
    print("type of ini_object", type(ini_string))

    # converting string to json
    final_dictionary = json.loads(ini_string)

    # printing final result
    print("final dictionary", str(final_dictionary))
    print("type of final_dictionary", type(final_dictionary))


# def convert(str):
if __name__ == '__main__':
    make_string()

#~00D0340;0;0;00000;0084;000;0273;;026;100
#~00D0101;499;2240
#~00D0270;499;1;2290;0000;00076;013

# Working with model no
# ~00D0011~00D016UPS102N2002N009
# ~00P003MODA1

# dict2 = {"~00P003MODA1" : "~00D0011~00D016UPS102N2002N009"}
# a2 = dict2["~00P003MODA1"]
# b2 = a2.split('~00D016')
# print(b2)

# # Working with battery status
# # ~00P003STB
# # ~00D0340;0;0;00000;0084;000;0273;;026;100
# dict3 = {"~00P003STB" : ['~00D0340','0','0','00000','0084','000','0273','','026','100']}
# a3 = dict3["~00P003STB"]
# _runtime = a3[4]
# runtime = int(_runtime)
# print(runtime)
#
# _battery_voltage = a3[6]
# battery_voltage = int(_battery_voltage)/10
# print(battery_voltage)
#
# _battery_temp = a3[8]
# battery_temp = int(_battery_temp)
# print(battery_temp)
#
# _battery_percentage = a3[9]
# battery_percentage = int(_battery_percentage)
# print(battery_percentage)

# Working with battery output
# ~00P003STO

# ~00D0270;499;1;2290;0000;00076;013
#
# dict4 = {"~00P003STO" : ['~00D0270','499','1','2290','0000','00076','013']}
# a4 = dict4["~00P003STO"]
#
# output_voltage = int(a4[3])/10
# print(output_voltage)
#
# load = int(a4[-1])
# print(load)
#
# # generating alerts
# if(output_voltage == 0 and load == 0):
#     alert = 1
# else:
#     alert = 0