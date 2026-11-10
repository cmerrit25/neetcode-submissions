class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for value in range(len(nums)):
            product = 1
            for i, num in enumerate(nums):
                if i != value:
                    product *= num
            output.append(product)

        return output
