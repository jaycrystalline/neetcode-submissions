class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for fi in range(len(nums)):
            fn = nums[fi]

            for mi in range(fi+1, len(nums)):
                if fn + nums[mi] == target:
                    return [fi, mi]

        return []