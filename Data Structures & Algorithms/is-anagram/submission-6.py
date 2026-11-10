class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        my_set1, my_set2 = dict(), dict()

        for i in range(len(s)):
            my_set1[s[i]] =  1 + my_set1.get(s[i], 0)
            my_set2[t[i]] =  1 + my_set2.get(t[i], 0)
        
        return my_set1 == my_set2