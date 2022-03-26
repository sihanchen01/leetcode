class Solution:
    def lemonadeChange(self, bills) -> bool:
        change = []
        for bill in bills:
            if bill == 20:
                if 5 in change and 10 in change:
                    change.remove(5)
                    change.remove(10)
                else:
                    return False
            elif bill == 10:
                if 5 in change:
                    change.remove(5)
                    change.append(10)
                else:
                    return False
            else:
                change.append(5)
        return True


s = Solution()
s.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5,
                 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
