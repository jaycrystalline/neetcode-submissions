class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = set()

        nums.sort()

        for n in nums:
            if n in count_map:
                return True
            count_map.add(n)
        
        return False