class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        flag = 0
        def lookaround(curr_ind, i, j, used):
            nonlocal flag
            if flag == 1: return

            if word[curr_ind] == board[i][j]:
                

                if curr_ind == len(word) - 1:
                    flag = 1

                    return
                
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni <= max_i and 0 <= nj <= max_j and [ni, nj] not in used:
                        lookaround(curr_ind + 1, ni, nj, used + [[ni, nj]])
        
        max_i = len(board) - 1
        max_j = len(board[0]) - 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    lookaround(0, i, j, [[i, j]])
                    if flag == 1:
                        return True


        return False
