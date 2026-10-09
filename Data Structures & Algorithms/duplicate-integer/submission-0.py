class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}

        for n in nums:
            if n in count_map:
                return True
            
            count_map[n] = None
        
        return False
