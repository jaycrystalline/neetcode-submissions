class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,-1,0,0,0,0,1,1,1,1,2]

        for f in range(len(nums) - 1):
            if f > 0 and nums[f] == nums[f-1]:
                continue

            s, l, r = 0, f + 1, len(nums) - 1

            while l < r:
                s = nums[f] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[f], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -=1
        
        return res
                        