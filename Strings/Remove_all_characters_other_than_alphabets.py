"""
Given a string S, remove all the characters other than the alphabets.

Example 1:

Input: S = "$Gee*k;s..fo, r'Ge^eks?"
Output: GeeksforGeeks
Explanation: Removed charcters other than
alphabets. 
 

Example 2:

Input:  S = "{{{}}> *& ^%*)"
Output: -1
Explanation: There are no alphabets.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function removeSpecialCharacter() which takes string S as input parameter and returns the resultant string. Return "-1" if no alphabets remain.

 

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)

 

Constraints:
1 <= |S| <= 105
"""

def removechar(s):
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans=""
    for char in s:
        if char in alphabets:
            ans +=char
    if len(ans)==0:
        return -1
    else:
        return ans
    
    
s=input()
print(removechar(s))