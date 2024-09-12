import cutie
import math
print("Convert from")
types = ["Decimal", "Binary","Hexadecimal"]
converting_from = cutie.select(types)
print("Convert to")
converting_to = cutie.select(types)
num = input("Input number: ")
final_answer = ""
if converting_from == 0:
    converting_from="Decimal"
elif converting_from == 1:
    converting_from="Binary"
elif converting_from == 2:
    converting_from="Hexadecimal"
if converting_to == 0:
    converting_to="Decimal"
elif converting_to == 1:
    converting_to="Binary"
elif converting_to == 2:
    converting_to="Hexadecimal"
    
#functions
def binary_to_decimal(num,final_answer):
    final_num = 0
    num = str(num) [::-1]
    for i in range(len(num)):
        final_num += int(num[i]) * (2**i)
    final_answer = str(final_num)
    print (final_answer)
def binary_to_hex(num, final_answer):
    binary_to_decimal(num, final_answer)
    print (hex(int(final_answer)))

def hex_to_decimal(num,final_answer):
    replace = ''
    num = str(num[::-1])
    for i in range(len(num)):
        str(i).replace("A", "10")
        print(i)
        i.replace("B", "11")
        i.replace("C", "12")
        i.replace("D", "13")
        i.replace("E", "14")
        i.replace("F", "15")
        final_answer += str(int(num[i]) * (16**i))
    print (final_answer)
def hex_to_binary(num, final_amswer):
    pass

#calling functions
if converting_from == "Decimal" and converting_to == "Binary":
    print (bin(int(num) ))
elif converting_from == "Decimal" and converting_to == "Hexadecimal":
    print (hex(num))
elif converting_from == "Binary" and converting_to == "Decimal":
    binary_to_decimal(num, final_answer)
elif converting_from == "Binary" and converting_to == "Hexadecimal":
    binary_to_hex(num, final_answer)
elif converting_from == "Hexadecimal" and converting_to == "Decimal":
    hex_to_decimal(num, final_answer)
elif converting_from == "Hexadecimal" and converting_to == "Binary":
    hex_to_binary(num) 
    