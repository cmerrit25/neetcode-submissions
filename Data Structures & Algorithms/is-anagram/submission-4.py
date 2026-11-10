class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_set1, my_set2 = dict(), dict()
        for element in s:
            my_set1[element] = my_set1.get(element, 1) + 1
        for element in t:
            my_set2[element] = my_set2.get(element, 1) + 1
        return my_set1 == my_set2