# Description

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input : s = "hello"
# Output :  "holle"

# *********************************************************************************************************

# MY SOLUTION

class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_list = []
        v_index = []
        count = 0
        for char in s:
            if char in vowels:
                v_list.append(char)
                v_index.append(count)
            count += 1
        v_index.reverse()
        for i, c in zip(v_index, v_list):
	    # CANT USE REPLACE
            s = s[:i] + c + s[i+1:]
        return s

# *********************************************************************************************************

# 双指针

class Solution2:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        res = list(s)
        start, end = 0, len(res)-1
        while start <= end:
            while start <= end  and res[start] not in vowels:
                start += 1
            while start <= end and res[end] not in vowels:
                end -= 1
            if start <= end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        return "".join(res)