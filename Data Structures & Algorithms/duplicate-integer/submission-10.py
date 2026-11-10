class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums: 
        #if num is already in set, then return True,
                if num in seen: 
                    return True
                    
                seen.add(num) #add nums to seen
        return False
        
           
        


            
            

             
        
            
        
            

        