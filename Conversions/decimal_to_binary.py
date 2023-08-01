"""
Given a decimal number N, compute its binary equivalent.

Example 1:

Input: N = 7
Output: 111
 

Example 2:

Input: N = 33
Output: 100001
    
"""


def decimal_to_binary(str):
    ans=bin(str)[2:]
    return ans
str=int(input())
print(decimal_to_binary(str))