
import  json

def make_string():
    str = ''
    for i in range(2):
     inp = input("Enter your data")
     out = '01AB'
     str += inp + ":" + out + " , "

    print(str)
    convert(str)

def convert(str):
    res = json.load(str)
    print(str(res))



if __name__ == '__main__':
    make_string()