from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # okay i am given a list of list which is the board as the input

        # lets try solving it with a brute force solution first, so i could iterate through ever row col and grid
        
        # i dont really want to solve that though as that is confusing my brain how to et up that triple for loop lol 

        # i think it gave me some insight though
        # if we do a pass over board for i and j
        #  we could then hash each position into a hashmap by a row or column
        # if when we hash there is a number in the row or column  already there or when we do a lookup of return false else return true

        rows = len(board)
        cols = len(board[0])
        
        rows_exist = defaultdict(list)
        cols_exist = defaultdict(list)
        squares_exist = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val != '.':
                    if r not in rows_exist[val]:
                        rows_exist[val].append(r)
                    else: 
                        return False
                    if c not in cols_exist[val]:
                        cols_exist[val].append(c)
                    else: 
                        return False
                    if (r // 3, c // 3) not in squares_exist[val]:
                        squares_exist[val].append((r//3, c//3))
                    else: 
                        return False
                else: 
                    continue
        return True
