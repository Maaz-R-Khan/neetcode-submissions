class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        frequency = set() #keep track of duplicates
        for num in nums: #loop over nums array
            if num in frequency: 
                return True
            
            frequency.add(num)
        return False