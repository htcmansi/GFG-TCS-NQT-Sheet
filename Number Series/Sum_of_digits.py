"""
Given a number, N. Find the sum of all the digits of N
 

Example 1:

Input:
N = 12
Output:
3
Explanation:
Sum of 12's digits:
1 + 2 = 3
Example 2:

Input:
N = 23
Output
5
Explanation:
Sum of 23's digits:
2 + 3 = 5

"""

def DigitSum(n):
    sum=0
    str_n=str(n)
    for digit in str_n:
        sum += int(digit)
    return sum
n=int(input())
print(DigitSum(n))