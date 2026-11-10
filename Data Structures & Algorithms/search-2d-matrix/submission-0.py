class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for s in matrix:
            for num in s:
                if num == target:
                    return True

        return False