"""
An integer number in base 10 which is divisible by the sum of its digits is said to be a Harshad Number. An n-Harshad number is an integer number divisible by the sum of its digit in base n.
Below are the first few Harshad Numbers represented in base 10:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20………
Given a number in base 10, our task is to check if it is a Harshad Number or not.

Examples : 

Input: 3
Output: 3 is a Harshad Number

Input: 18
Output: 18 is a Harshad Number

Input: 15
Output: 15 is not a Harshad Number

 """
 
 
def is_HarshedNumber(num):
    string=str(num)
    sum=0
    for digit in string:
        sum += int(digit)
        
    if(num % sum)==0:
        return 'is Harshed Number'
    else:
        return 'is not Harshed Number'
    
num=int(input())
print(num,is_HarshedNumber(num))
               
     