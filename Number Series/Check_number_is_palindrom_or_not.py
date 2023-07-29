"""
Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.
Note:A Palindrome number is a number which stays the same when reversed.Example- 121,131,7 etc.

Example 1:

Input:
N=56
Output:
1
Explanation:
The digit sum of 56 is 5+6=11.
Since, 11 is a palindrome number.Thus,
answer is 1.
Example 2:

Input:
N=98
Output:
0
Explanation:
The digit sum of 98 is 9+8=17.
Since 17 is not a palindrome,thus, answer
is 0.
    
"""

def isDigitSumPalindrome(N):
        N_str=str(N)
        digit_sum=sum(int(digit) for digit in N_str)
        digit_sum_str=str(digit_sum)
        reverse_str=digit_sum_str[::-1]
        if digit_sum_str==reverse_str:
            return 1
        else:
            return 0
        
N=int(input())
print(isDigitSumPalindrome(N))