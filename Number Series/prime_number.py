"""
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.
 

Example 1:

Input:
N = 5
Output:
1
Explanation:
5 has 2 factors 1 and 5 only.
Example 2:

Input:
N = 25
Output:
0
Explanation:
25 has 3 factors 1, 5, 25
    
"""
import math
def isPrime (N):
    if N < 2:
        return 0
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return 0
    
    return 1

N=int(input())
print(isPrime(N))