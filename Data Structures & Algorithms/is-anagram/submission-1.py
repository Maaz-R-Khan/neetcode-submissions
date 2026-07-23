class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # U - check if all characters in both strings are the same return true, 
        #if any character is different return false

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t and len(sorted_s) == len(sorted_t): 
            return True
        else: 
            return False
        