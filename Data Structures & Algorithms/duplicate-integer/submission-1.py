class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for element in nums:
            try:   
                my_map[element] == 1
                return True
            except KeyError:
                my_map[element] = 1
        return False