class Solution:
    def stringMatching(self, words):
        ans = []
        # DEBUG: use index to avoid double use of words
        # for word in words:
        #   for check in words:
        #     if word in check:
        #       ans.append(word)
        for i in range(len(words)):
            for check in words[:i]+words[i+1:]:
                if words[i] in check:
                    ans.append(words[i])
                    break   # to avoid double add word into ans
        return ans


s = Solution()
s.stringMatching(["mass", "as", "hero", "superhero"])
