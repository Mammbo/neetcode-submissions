class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # i am given a 2d grid where a 1 repersents land and a 0 repersents water
        # i need to return an integer that count the total number of islands

        # since i am given the matrix i do not need to make the graph all the information i need is in the matrix.

        # islands can only be formed by connected adjacent lands horizontally or vertically 


        # i think we should write out the general for loop to traverse this and then we can write out the dfs function
        # looking at the constraints the length of the grid will never be a super large number so we can do recursion on it
        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != '1':
                return
            grid[r][c] = 0
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(r + dr, c + dc)
        
        rows, cols = len(grid), len(grid[0])

        ans = 0
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans




