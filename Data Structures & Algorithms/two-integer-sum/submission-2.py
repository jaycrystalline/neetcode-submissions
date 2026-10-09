class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen_map:
                return [seen_map[diff], i]

            seen_map[n] = i