class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """return the size of the longest substring containing each vowel an even number of times"""
        index = {0: -1}
        vowels = 'aeiou'
        state = ans = 0
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:
                state ^= 1 << j
            if state not in index:
                index[state] = i
            ans = max(ans, i - index[state])
        return ans
