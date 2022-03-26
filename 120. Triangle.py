class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]


s = Solution()
s.minimumTotal([[1], [-2, -5], [3, 6, 9], [-1, 2, 4, -3]])
