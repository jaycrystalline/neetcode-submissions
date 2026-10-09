class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # print(f"for: {chars}, max_length={max_length}")
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
                # print(f"chars={chars}, left={left}, right={right}")
            
            chars.add(s[right])
            max_length = max(max_length, len(chars))
        
        return max_length


# s="abcabcbb"