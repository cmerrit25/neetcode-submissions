class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            try:
                dups[num] += 1
                return True
            except KeyError:
                dups[num] = 1
        return False

        