"""
For an input year N, find whether the year is a leap or not. 
 

Example 1:

Input:
N = 4
Output:
1
Explanation:
4 is not divisible by 100
and is divisible by 4 so its
a leap year
Example 2:

Input:
N = 2021
Output:
0
Explanation:
2021 is not divisible by 100
and is also not divisible by 4
so its not a leap year
    
"""
def isleap(N):
    if N % 4 ==0:
        if N % 100 ==0:
            if N % 400 ==0:
                return  1
            else:
                return 0
        else:
            return 1
    else:
        return 0
N=int(input())
print(isleap(N))