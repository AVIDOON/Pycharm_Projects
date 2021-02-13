import json

# Working with model no
# ~00D0011~00D016UPS102N2002N009
# ~00P003MODA1
def selecting_data():
    json_dict = {}
    params = {}
    actual_dict = {"~00P003MODA1" : "~00D0011~00D016UPS102N2002N009",
                   "~00P003RATA8": ['~00D064230', '500', '230', '500', '1000', '0900', '', '080', '280', '090', '080', '280', '270', '0', '024', '400', '700'],
                   "~00P003STB" : ['~00D0340','0','0','00000','0084','000','0273','','026','100'],
                   "~00P003STO" : ['~00D0270','499','1','2290','0000','00076','013'],
                   "~00P003STI": ['~00D0101','499','2240']}
    # 2290
    # dict2 = {"~00P003MODA1" : "~00D0011~00D016UPS102N2002N009"}
    a2 = actual_dict["~00P003MODA1"]
    ups_data = a2.split('~00D016')
    ups_model = ups_data[1]

    json_dict["model_number"] = ups_model

    # working with frequency, voltage and powersupply
    # data_dict = {}
    # new_dict =  {'~00P003RATA8': ['~00D064230', '500', '230', '500', '1000', '0900', '', '080', '280', '090', '080', '280', '270', '0', '024', '400', '700']}
    a = actual_dict['~00P003RATA8'][1]
    freq_in_Hz = int(a)/10
    params["freq (in Hz)"] = freq_in_Hz

    #
    b = actual_dict['~00P003RATA8'][2]
    voltage_in_volts = int(b)
    params["Voltage (in Volts)"] = voltage_in_volts

    #
    c = actual_dict['~00P003RATA8'][5]
    power_supply = int(c)/100
    params["Power supply (in KWs)"] = power_supply


    # print(data_dict)

    # working with STI
    d = actual_dict["~00P003STI"]
    # input frequency
    input_freq_in_Hz = int(d[1])/10
    params["input_frequency_in_Hz"] = input_freq_in_Hz

    #input voltage
    input_voltage = int(d[2])/10
    params["input_voltage"] = input_voltage


    # # Working with battery status
    # # ~00P003STB
    # # ~00D0340;0;0;00000;0084;000;0273;;026;100
    # dict3 = {"~00P003STB" : ['~00D0340','0','0','00000','0084','000','0273','','026','100']}
    a3 = actual_dict["~00P003STB"]

    runtime = int(a3[4])
    params["runtime"] = runtime

    #
    battery_voltage = int(a3[6])/10
    params["battery_voltage"] = battery_voltage

    battery_temp = int(a3[8])
    params["battery_temp"] = battery_temp
    #

    battery_percentage = int(a3[9])
    params["battery_percentage"] = battery_percentage


    # Working with battery output
    # ~00P003STO

    # ~00D0270;499;1;2290;0000;00076;013
    #
    # dict4 = {"~00P003STO" : ['~00D0270','499','1','2290','0000','00076','013']}

    a4 = actual_dict["~00P003STO"]

    output_voltage = int(a4[3])/10
    params["output_voltage"] = output_voltage

    load = int(a4[-1])
    params["load"] = load
    #
    # generating alerts
    if(output_voltage == 0 or load == 0):
        alerts = 1
    else:
        alerts = 0

    json_dict["params"] = params

    json_dict["alerts"] = alerts
    # calling the function to convert into json
    convert_string_to_json(json_dict)
    # print(json_dict)

def convert_string_to_json(json_dict):
    ini_string = json.dumps(json_dict)
    # print("initial 1st dictionary", ini_string)
    # print("type of ini_object", type(ini_string))

    # converting string to json
    final_dictionary = json.loads(ini_string)

    # printing final result
    print("final dictionary : ", str(final_dictionary))
    # print("type of final_dictionary", type(final_dictionary))

# Function to make a string dictionary
# def make_string_dictionary():
#     dict = {}
#     inp = input("Enter input ")
#     # out = response
#     out = input('Enter output')
#     if(out.__contains__(";")):
#         out = out.split(';')
#     dict[inp] = out
#     return dict

if __name__ == '__main__':
    # call make_string_dictionary after every response
    selecting_data()