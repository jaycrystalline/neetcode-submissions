class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time O(n), Space O(n)
        seen_numbers = set()
        nums.sort()

        for n in nums:
            if n in seen_numbers:
                return True
    
            seen_numbers.add(n)
        
        return False