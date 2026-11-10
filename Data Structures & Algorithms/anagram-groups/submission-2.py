class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = {}
        output = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if not sorted_word in sort_dict:
                sort_dict[sorted_word] = []
            sort_dict[sorted_word].append(word) 

        for value in sort_dict.values():
            output.append(value)
        return sorted(output, key=len)