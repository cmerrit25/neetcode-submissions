class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_set1, my_set2 = dict(), dict()
        for element in s:
            try:
                my_set1[element] += 1
            except KeyError:
                my_set1[element] = 1
        for element in t:
            try:
                my_set2[element] += 1
            except KeyError:
                my_set2[element] = 1
        if my_set1 == my_set2:
            return True
        return False