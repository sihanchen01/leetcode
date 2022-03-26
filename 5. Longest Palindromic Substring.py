# MY SOLUTION:
# BRUTE FORCE 
# TC: O(n**3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        i = 0
        result =[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j][::-1] == s[i:j]:
                    result.append(s[i:j])
        result.sort(key=lambda s: len(s))
        return result[-1]

# ******************************************************

# BEST ANSWER

def longestPalindrome(self, s):
    lenS = len(s)
    if lenS <= 1: return s
    minStart, maxLen, i = 0, 1, 0
    while i < lenS:
        if lenS - i <= maxLen / 2: break
        j, k = i, i
        while k < lenS - 1 and s[k] == s[k + 1]: k += 1
        i = k + 1
        while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1
        if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
    return s[minStart: minStart + maxLen]
