"""
Write a program to reverse the digits of an integer.

Input : num = 12345
Output: 54321

Input : num = 876
Output: 678
    
"""

def revreseDigits(N):
    str_n=str(N)
    reverse_num=str_n[::-1]
    return int(reverse_num)

N=int(input())
print(revreseDigits(N))
    