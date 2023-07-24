"""
Given a string, The task is to count the number of alphabets present in the string.

Example 1:

Input:
S = "adjfjh23"
Output: 6
Explanation: only last 2 are not 
alphabets.
Example 2:

Input:
S = "n0ji#k$"
Output: 4
Explanation: #, $, 0 are not alphabets.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function Count() which takes the string S as inputs and returns alphabets count.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105
S contains only upper and lower case alphabets, digits and '#', '!', '$', '&' only.
"""

def countAlphabets(s):
    count=0
    
    for char in s:
        if char.isalpha():
            count +=1
    return count
    
s=input()
print(countAlphabets(s))