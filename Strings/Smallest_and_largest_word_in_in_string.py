"""
Given a string, find the minimum and the maximum length words in it. 

Examples: 

Input : "This is a test string"
Output : Minimum length word: a
         Maximum length word: string

Input : "GeeksforGeeks A computer Science portal for Geeks"
Output : Minimum length word: A
         Maximum length word: GeeksforGeeks
"""


def SmallLargeWord(s):
    words=s.split()
    small_word=min(words,key=len)
    large_word=max(words,key=len)
    return small_word,large_word

s=input()
print(SmallLargeWord(s))
