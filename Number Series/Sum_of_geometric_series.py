"""
A Geometric series is a series with a constant ratio between successive terms. The first term of the series is denoted by a and common ratio is denoted by r. The series looks like this :- a, ar, ar2, ar3, ar4, . . .. The task is to find the sum of such a series. Examples :

Input : a = 1
        r = 0.5
        n = 10
Output : 1.99805

Input : a = 2
        r = 2
        n = 15
Output : 65534
A Simple solution to calculate the sum of geometric series. 
    
"""
    
    
def SumOfGS(a,r,n):
    if r == 1:
        return float('inf')
    else:
        sum=int(a*(1-r**n)/(1-r))
        return sum
a=int(input())
r=input()
n=int(input())
sum=SumOfGS(a,r,n)
print(sum)