"""
Find the number of factors for a given integer N.
 

Example 1:

Input:
N = 5
Output:
2
Explanation:
5 has 2 factors 1 and 5
Example 2:

Input:
N = 25
Output:
3
Explanation:
25 has 3 factors 1, 5, 25

"""

def countFactors (N):
        count = 0
        i = 1
        while i * i <= N:
            if N % i == 0:
                if i * i == N:
                    count += 1
                else:
                    count += 2
            i += 1
        return count
    
N=int(input())
print(countFactors(N))