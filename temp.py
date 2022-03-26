class Solution:
    river_size = 0
    ans = []

    def riverSizes(self, matrix):
        # Write your code here.
        row_size = len(matrix)
        col_size = len(matrix[0])
        for row in range(row_size):
            for col in range(col_size):
                self.cal_river_size(
                    matrix, row, col, row_size, col_size)
                self.ans.append(
                    self.river_size) if self.river_size != 0 else None
                self.river_size = 0
        return self.ans

    def cal_river_size(self, matrix, row, col, row_size, col_size) -> int:
        """Given a matrix and row col for a point, return size of river"""
        if 0 <= row < row_size and 0 <= col < col_size:
            if matrix[row][col] == 1:
                self.river_size += 1
                matrix[row][col] = 0
                self.cal_river_size(matrix, row-1,
                                    col, row_size, col_size)
                self.cal_river_size(matrix, row+1,
                                    col, row_size, col_size)
                self.cal_river_size(matrix, row,
                                    col-1, row_size, col_size)
                self.cal_river_size(matrix, row,
                                    col+1, row_size, col_size)


s = Solution()
# print(s.riverSizes([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [
#     0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]))

print(s.riverSizes([
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1]
]))
