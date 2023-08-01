"""
The problem is to convert the given binary number (represented as string) to its equivalent octal number. The input could be very large and may not fit even into unsigned long long int.

Examples:  

Input : 110001110
Output : 616

Input  : 1111001010010100001.010110110011011
Output : 1712241.26633 
    
"""



def binary_to_octal(str):
    decimal=int(str,2)
    octal=oct(decimal)[2:]
    return octal
str=input()
print(binary_to_octal(str))