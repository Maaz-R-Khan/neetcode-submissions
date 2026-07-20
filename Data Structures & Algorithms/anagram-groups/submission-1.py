class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # U - given list of anagrams, return sublists of anagrams
        # p - loop through strs, check one element against another and if its a 
        # an anagram, add it to a sublist, after loop is finished return the sublist


        """
        anagram - same characters, and must be same length
        edge cases - 
        1) list with one element, return the element
        2) empty list, return an empty list
        """

        if len(strs) == 1: 
            return [strs]
        
        # if strs == []: 
        #     return strs

        groups = {}
        
        strs.sort() 

        for i in strs:
            sorted_string = sorted(i) #sorts each strings
            key = "".join(sorted_string) # create the sorted string to use as key
            groups.setdefault(key, []).append(i) #if key doesn't exist, create it and empty list as value and append i

        return list(groups.values())


            
                

            