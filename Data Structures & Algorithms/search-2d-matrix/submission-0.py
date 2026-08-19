class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == target:
                    return True
        return False