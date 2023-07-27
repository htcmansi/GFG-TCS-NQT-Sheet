"""
Given a number N, the task is to find the largest prime factor of that number.
 Example 1:

Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor i.e 5 only.
Example 2:

Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 2 and 3 in which 3 is greater.
    
"""

def largePrimeFactor(n):
    factors=[]
    divisor=2
    
    while n>1 and divisor * divisor <=n:
        if (n % divisor)==0:
            factors.append(divisor)
            n //=divisor
        else:
            divisor +=1
            
    if n>1:
        factors.append(n)
    return max(factors)

n=int(input())
print(largePrimeFactor(n))