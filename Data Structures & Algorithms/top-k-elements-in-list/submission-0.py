class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        output = []
        for num in nums:
            try:
                res[num] += 1
            except KeyError:
                res[num] = 1
        new_res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse = True)}
        i = 0
        for key in new_res.keys():
            output.append(key)
            i += 1
            if i >= k:
                break
        output.sort()
        return output