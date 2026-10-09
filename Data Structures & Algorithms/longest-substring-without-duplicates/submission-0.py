class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        tmp = set()
        max_length = 0

        while i < len(s):
            j = i

            while s[j] not in tmp and j < len(s):
                tmp.add(s[j]) # zxy
                j += 1
            

            max_length = max(max_length, len(tmp))
            print(tmp, s[i], i, max_length)
            tmp.remove(s[i])

            i += 1
        
        return max_length