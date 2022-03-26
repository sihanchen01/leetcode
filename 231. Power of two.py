class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n % 2 == 0:
            self.isPowerOfTwo(n/2)
        else:
            if n == 1:
                return True
            return False


s = Solution()
print(s.isPowerOfTwo(16))
