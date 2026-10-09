class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for n in nums:
            if n not in count_map:
                count_map[n] = 1
                continue
            
            count_map[n] += 1
            
        sd = dict(sorted(count_map.items(), key=lambda item: item[1]))

        return list(sd.keys())[-k:]