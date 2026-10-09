class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [set() for _ in range(len(nums))]
        print(freq)
        for n in nums:
            count[n] = count.get(n, 0) + 1
            freq[count.get(n)-1].add(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result
