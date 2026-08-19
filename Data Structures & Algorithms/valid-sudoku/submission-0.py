class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        L = []
        for i in range(9):
            L.append(board[i])
        
        for x in range(9):
            T = []
            for y in range(9):
                T.append(board[y][x])
            L.append(T)
        for q in range(3):
            for w in range(3):
                P = []
                q = q
                w = w
                for z in range(3):
                    for a in range(3):
                        P.append(board[q * 3 + z][w * 3 + a])
                L.append(P)
        
        check = ['1', '2', '3', '4', '5' , '6', '7', '8', '9', '.']
        for sud in L:
            for char in sud:
                if char not in check:
                    return False
            kropki = sud.count('.')
            if kropki + len(set(sud)) - 1 != 9:
                return False
        return True