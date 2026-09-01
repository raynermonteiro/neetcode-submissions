class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        seenSet = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (i < 0 or j < 0 or i >= ROW or j>= COL or word[k] != board[i][j]) or (i, j) in seenSet:
                return False

            seenSet.add((i, j))

            result = (dfs(i+1, j, k+1) or
            dfs(i-1, j, k+1) or
            dfs(i, j+1, k+1) or
            dfs(i, j-1, k+1))

            seenSet.remove((i, j))
            return result

        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] != word[0]:
                    continue
                if dfs(i, j, 0):
                    return True
        
        return False
        