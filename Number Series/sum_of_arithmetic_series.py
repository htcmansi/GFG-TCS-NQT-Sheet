"""
A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.

 

Example 1:

Input: n = 5, a = 1, d = 3
Output: 35
Explanation: Series upto 5th term is
1 4 7 10 13, so sum will be 35.
Example 2:

Input: n = 3, a = 1, d = 2
Output: 9
Example: Series upto 3rd term is 
1 3 5, so sum will be 9.

"""
def sumOfAp(n,a,d):
    return int((n/2)*(2*a+(n-1)*d))
n=int(input())
a=int(input())
d=int(input())
sum=sumOfAp(n,a,d)
print(sum)
