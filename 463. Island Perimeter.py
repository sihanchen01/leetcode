# 463. Island Perimeter

# MY SOLUTION:

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        
        # find perimeter of each square that connected to water.(since there is no lake)
        total = 0
        for row in range (len(grid)):
            for col in range (len(grid[0])):
                if grid[row][col] == 1:
                    total += [grid[row][max(0,col-1)], 
                         grid[row][min(len(grid[0])-1,col+1)], 
                         grid[max(0,row-1)][col], 
                         grid[min(len(grid)-1, row+1)][col]].count(0)
                    
        # now add in border squares
        total += (grid[0][0] + grid[0][len(grid[0])-1] + grid[len(grid)-1][0] + grid[len(grid)-1][len(grid[0])-1]) * 2 + (grid[0][1:len(grid[0])-1]).count(1) + (grid[len(grid)-1][1:len(grid[0])-1]).count(1)
        border_col_list = []
        for row in range(1, len(grid)-1):
            border_col_list.append(grid[row][0])
            border_col_list.append(grid[row][len(grid[0])-1])
        total += border_col_list.count(1)
        return total

# ***************************************************************************************************************************

class Solution2:
    def islandPerimeter(self, grid) -> int:
            l1,l2 = len(grid),len(grid[0])
            ans = 0
            
            for i in range(l1):
                for j in range(l2):
                    #for every cell, initialize the adjacent to 0
                    adj = 0
                    
                    if grid[i][j] == 1:
                        for x,y in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                            #we plus adj with 1 for (up,down,left,right) which in valid grid
                            if l1> x >= 0 and l2> y >= 0 and grid[x][y] == 1:
                                adj += 1
                        ans += 4 - adj
            return ans

# ***************************************************************************************************************************

class Solution3:

    def islandPerimeter(self, grid):
            grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
            grid_trans = list(map(list, zip(*grid)))
            grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
            return sum(row.count('01') + row.count('10') for row in grid_ext)

    # OR
    # *(BEST)
class Solution4:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        grid_r = ['0'+''.join(str(r) for r in row)+'0' for row in grid]
        grid_c = ['0'+''.join(str(c) for c in col)+'0' for col in zip(*grid)]
        return sum(row.count('01')+row.count('10') for row in grid_r+grid_c)