"""
Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6
Example 2:

Input:
n = 4
arr[] = {1 2 3 4}
Output: 10
Your Task:
You need to complete the function sumElement() that takes arr and n and returns the sum. The printing is done by the driver code.

"""


def sumElement(arr,n):
    sumElement = sum(arr)
    return sumElement


#Driver Code Starts
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
#Driver Code Ends