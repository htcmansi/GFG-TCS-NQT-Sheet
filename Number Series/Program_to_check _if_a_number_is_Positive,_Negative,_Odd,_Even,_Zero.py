"""
Given a number n, the task is to check whether the given number is positive, negative, odd, even, or zero.
Input : 10
Output : Positive number is even

Input : 0
Output : is Even    
    
"""

def checkNumber(num):
    if num >0:
        if (num % 2)==0:
            return 'Positive Number is even'
        else:
            return 'Positive Number is odd'
    elif num <0:
        if (num %2)==0:
            return 'Negative Numberis even'
        else:
            return 'Negative Number is odd'
    else:
        return 'Zero is even number'
    
num =int(input())
print(checkNumber(num))