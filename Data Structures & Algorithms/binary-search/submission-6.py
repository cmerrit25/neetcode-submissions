class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:

        # if search is invalid return -1
        if l > r:
            return -1

        # search for middle value of requested sublist
        m = l + (r - l) // 2
        
        # if middle value is target return index
        if nums[m] == target:
            return m

        # if target is to right of middle value search all values to the right
        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        
        # else search all values to the left of the value
        return self.binary_search(l, m - 1, nums, target)

    # recursively calling search function
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)